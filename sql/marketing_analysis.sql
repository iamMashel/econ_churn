-- Campaign Effectiveness

SELECT 
    campaign_id,
    COUNT(*) AS sent,
    SUM(CASE WHEN clicked THEN 1 ELSE 0 END) AS clicks,
    SUM(CASE WHEN converted THEN 1 ELSE 0 END) AS conversions,
    ROUND(100.0 * SUM(CASE WHEN converted THEN 1 ELSE 0 END) / COUNT(*), 2) AS conversion_rate
FROM campaigns
GROUP BY campaign_id;
