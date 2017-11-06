drop table resampled;
CREATE TABLE resampled (LIKE five_min_summary INCLUDING ALL);

INSERT INTO resampled
SELECT * FROM five_min_summary;

INSERT INTO resampled
SELECT * FROM fifteen_min_summary;

INSERT INTO resampled
SELECT * FROM thirty_min_summary;

INSERT INTO resampled
SELECT * FROM hourly_summary;

INSERT INTO resampled
SELECT * FROM four_hour_summary;

INSERT INTO resampled
SELECT * FROM daily_summary;

INSERT INTO resampled
SELECT * FROM weekly_summary;

INSERT INTO resampled
SELECT * FROM monthly_summary;

INSERT INTO resampled
SELECT * FROM yearly_summary;