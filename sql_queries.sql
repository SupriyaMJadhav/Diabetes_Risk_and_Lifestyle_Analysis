CREATE DATABASE DiabeteaDB;
---- Import diabetes_cleaned_final.csv in Database

USE DiabetesDB;
SELECT TOP 10 * FROM diabetes_cleaned_final;

SELECT 
    gender, 
    risk_tier, 
    COUNT(*) AS patient_count
FROM diabetes_cleaned_final
GROUP BY gender, risk_tier
ORDER BY gender, patient_count DESC;

SELECT 
    physical_activity, 
    diet_quality, 
    ROUND(AVG(risk_score), 2) AS average_risk
FROM diabetes_cleaned_final
GROUP BY physical_activity, diet_quality
ORDER BY average_risk DESC;

SELECT 
    patient_id, 
    age, 
    bmi, 
    glucose_level, 
    risk_score
FROM diabetes_cleaned_final
WHERE diabetes_outcome = 0 AND risk_tier = 'High'
ORDER BY risk_score DESC;

SELECT 
    age_group,
    COUNT(*) AS total_patients,
    SUM(CASE WHEN glucose_level > 140 THEN 1 ELSE 0 END) AS high_glucose_count,
    SUM(CASE WHEN hba1c > 6.0 THEN 1 ELSE 0 END) AS high_hba1c_count
FROM diabetes_cleaned_final
GROUP BY age_group;