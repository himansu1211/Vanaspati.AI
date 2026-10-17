import React from 'react';
import DiseaseInfoCard from '../components/DiseaseInfoCard';
import GeneratePdfFile from './GeneratePdfFile';

const DiseaseDetails = (props) => {
  const { predictedDiseaseData } = props;
  if (!predictedDiseaseData) return null;

  const toList = (field) => {
    if (!field) return [];
    if (Array.isArray(field)) return field;
    if (typeof field === 'object') return Object.values(field);
    return [String(field)];
  };

  const symptoms = toList(predictedDiseaseData.disease_symptoms);
  const causes = toList(predictedDiseaseData.disease_causes);
  const prevention = toList(predictedDiseaseData.disease_prevention);
  const fertilizer = toList(predictedDiseaseData.fertilizer_recommendation);
  const pesticides = toList(predictedDiseaseData.pesticides_and_fungicides);
  const organic = toList(predictedDiseaseData.organic_remedies);
  const control = toList(predictedDiseaseData.disease_control);

  return (
    <div className='disease-details'>
        <GeneratePdfFile data={predictedDiseaseData}/>
        
        <div className="disease-header-info">
          <h1>Plant: {predictedDiseaseData.plant_name || (predictedDiseaseData.idName ? predictedDiseaseData.idName.split('___')[0].replace(/_/g, ' ') : 'Botanical Specimen')} <span style={{ fontSize: '0.85rem', color: '#1b4332', background: 'rgba(45, 106, 79, 0.12)', padding: '3px 8px', borderRadius: '6px', fontWeight: 600 }}>✓ Verified Identification</span></h1>
          <h2>Condition: {predictedDiseaseData.disease_name}</h2>

          
          <div className="badge-container" style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', margin: '8px 0 16px' }}>
            {predictedDiseaseData.pathogen_type && (
              <span className="badge pathogen-badge" style={{ background: '#f1f5f9', color: '#334155', border: '1px solid #e2e8f0', padding: '4px 10px', borderRadius: '6px', fontSize: '0.82rem', fontWeight: 600 }}>
                🔬 {predictedDiseaseData.pathogen_type}
              </span>
            )}
            {predictedDiseaseData.scientific_name && (
              <span className="badge scientific-badge" style={{ background: '#f8fafc', color: '#475569', border: '1px solid #e2e8f0', padding: '4px 10px', borderRadius: '6px', fontSize: '0.82rem', fontStyle: 'italic', fontWeight: 600 }}>
                🧬 {predictedDiseaseData.scientific_name}
              </span>
            )}
            {predictedDiseaseData.severity && (
              <span className="badge severity-badge" style={{ background: '#fef2f2', color: '#991b1b', border: '1px solid #fecaca', padding: '4px 10px', borderRadius: '6px', fontSize: '0.82rem', fontWeight: 600 }}>
                ⚠️ {predictedDiseaseData.severity}
              </span>
            )}
          </div>
        </div>

        {symptoms.length > 0 && (
          <DiseaseInfoCard title="1. Observed Symptoms" data={symptoms} />
        )}
        
        {causes.length > 0 && (
          <DiseaseInfoCard title="2. Causes & Disease Etiology" data={causes} />
        )}
        
        {prevention.length > 0 && (
          <DiseaseInfoCard title="3. Preventive Cultural Practices" data={prevention} />
        )}

        {fertilizer.length > 0 && (
          <DiseaseInfoCard title="4. Fertilizer & Soil Nutrition Protocols" data={fertilizer} />
        )}

        {pesticides.length > 0 && (
          <DiseaseInfoCard title="5. Chemical Pesticides, Fungicides & Insecticides" data={pesticides} />
        )}

        {organic.length > 0 && (
          <DiseaseInfoCard title="6. Organic & Biological Remedies" data={organic} />
        )}

        {control.length > 0 && (
          <DiseaseInfoCard title="7. Action Plan & Cure Steps" data={control} />
        )}
    </div>
  );
};

export default DiseaseDetails;