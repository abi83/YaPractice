SELECT
	sin_souts.id AS Zayavka,
    cities.city AS City,
    smis.name AS SmiName,
    scores.data AS ScoreDate,
    scores.number_score AS ScoreNum,
    score_rows.name AS ScoreText,
    score_rows.smi_id AS SmiID
FROM
    sin_souts
JOIN
    score_rows
ON
    sin_souts.id_in = score_rows.id OR sin_souts.id_out = score_rows.id
JOIN
    smis
ON
    smis.id = score_rows.smi_id
JOIN
    cities
ON
    cities.id = smis.id_city
JOIN
    scores
ON
    scores.id = score_rows.score_id
WHERE
    cities.population > 100000 AND cities.population < 500000
ORDER BY
	Zayavka


SELECT
    sin_souts.id AS Zayavka,
    SuplierScore.name AS SuplierScoreText,
    CustomerScore.name AS CustomerScoreText,
FROM
    sin_souts
JOIN
    score_rows AS SuplierScore
ON
    sin_souts.id_in = SuplierScore.id
JOIN
    score_rows AS CustomerScore
ON
    sin_souts.id_out = CustomerScore.id
LIMIT 100