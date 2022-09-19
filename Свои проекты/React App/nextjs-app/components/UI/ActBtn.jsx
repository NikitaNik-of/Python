import React from 'react'

const ActBtn = ({children, ...props}) => {
  return (
    <button {...props} className=" box-content bg-teal-200 border-teal-300 rounded-2xl px-3 py-1 border-2 hover:bg-teal-100 hover:border-teal-400 transition-colors">
      {children}
    </button>
  )
}

export default ActBtn