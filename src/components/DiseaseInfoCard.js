import React from 'react'

const DiseaseInfoCard = (props) => {
    return (
        <div className='Disease-info-card'>
            <h1>{props.title}</h1>
            {props.data.map((item, index) => (
                <li key={index}>{item}</li>
            ))}
        </div>
    )
}

export default DiseaseInfoCard