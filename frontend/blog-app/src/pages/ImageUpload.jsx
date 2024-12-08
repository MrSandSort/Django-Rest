import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Upload, message, Image as AntImage } from 'antd';
import { InboxOutlined } from '@ant-design/icons';

const { Dragger } = Upload;

const ImageUploader = () => {
  const [images, setImages] = useState([]);
  const [uploading, setUploading] = useState(false);
  const [profilePicture, setProfilePicture] = useState(null); // State for profile picture

  const fetchImages = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/user/images/');
      setImages(response.data);
    } catch (error) {
      message.error('Failed to fetch images');
      console.error('Error fetching images:', error);
    }
  };

  useEffect(() => {
    fetchImages();
  }, []);

  const handleUpload = async (info) => {
    const { file } = info;

    if (file.status === 'uploading') {
      setUploading(true);
    }

    if (file.status === 'done') {
      setUploading(false);
      message.success(`${file.name} file uploaded successfully.`);
      fetchImages();
    } else if (file.status === 'error') {
      setUploading(false);
      message.error(`${file.name} file upload failed.`);
    }
  };

  const onChange = async (info) => {
    const { file } = info;
    
    // Handle uploading with FormData
    if (file.status === 'uploading') {
      setUploading(true);
      const formData = new FormData();
      formData.append('image', file.originFileObj);

      try {
        const response = await axios.post('http://127.0.0.1:8000/user/images/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        
        message.success(`${file.name} uploaded successfully`);
        fetchImages();
      } catch (error) {
        setUploading(false);
        message.error(`Upload failed: ${file.name}`);
        console.error('Upload error:', error);
      }
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-2xl mb-4">Image Uploader</h2>

      {profilePicture && (
        <div className="mb-4">
          <h3 className="text-lg font-semibold mb-2">Profile Picture</h3>
          <div className="flex justify-center">
            <AntImage
              width={150}
              height={150}
              src={profilePicture}
              alt="Profile Picture"
              className="rounded-full object-cover"
            />
          </div>
        </div>
      )}

      <Dragger
        name="image"
        multiple={false}
        onChange={onChange} // Using onChange for file upload
        disabled={uploading}
        className="mb-4"
      >
        <p className="ant-upload-drag-icon">
          <InboxOutlined />
        </p>
        <p className="ant-upload-text">Click or drag file to upload</p>
        <p className="ant-upload-hint">
          Support for a single image upload. Strictly prohibit from uploading company data or other sensitive files.
        </p>
      </Dragger>

      <div className="grid grid-cols-3 gap-4">
        {images.map((img) => (
          <div
            key={img.id}
            className="border rounded p-2 cursor-pointer hover:shadow-md transition"
            onClick={() => setProfilePicture(img.image_url)} 
          >
            <AntImage
              width="100%"
              src={img.image_url}
              alt={`Uploaded at ${img.uploaded_at}`}
              className="object-cover"
            />
            <p className="text-sm text-gray-500 mt-2">
              Uploaded: {new Date(img.uploaded_at).toLocaleString()}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ImageUploader;
