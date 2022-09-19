import React from 'react'

const InactBtn = ({children, ...props}) => {
  return (
    <button {...props} className=" box-content bg-transparent border-transparent rounded-2xl px-3 py-1 border-2 hover:bg-gray-200 transition-colors">
        {children}
    </button>
  )
}

export default InactBtn