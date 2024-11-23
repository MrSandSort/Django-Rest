import React from 'react'
import { Progress } from 'reactstrap'

export default function ProgressBar() {
  return (
    <div>
      <Progress multi>
        <Progress bar value={20} color='success' animated={true}>Wow!</Progress>

      </Progress>
    </div>
  )
}
