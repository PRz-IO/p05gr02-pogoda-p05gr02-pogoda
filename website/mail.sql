SELECT user.email, user.id as id_uzytkownika, miasto.nazwa_miasta, miasto.id as id_miasta FROM user, miasto, Miasto_Uzytkownika
WHERE user.id = Miasto_Uzytkownika.id_uzytkownika AND miasto.id = Miasto_Uzytkownika.id_miasta;

SELECT date(pd.data) as dzień, pd.min_temp, pd.max_temp, m.nazwa_miasta, s.stan_pogody
FROM pogoda_dzienna AS pd, miasto AS m, stanpogody AS s
WHERE pd.id_miasta = m.id AND pd.id_stan_pogody = s.id AND date(data) BETWEEN date('now') AND date('now','+6 days');

--SELECT m.nazwa_miasta, u.email, u.username, pd.min_temp, pd.max_temp, s.stan_pogody
--FROM miasto AS m, user AS u, pogoda_dzienna AS pd, stanpogody AS s
--WHERE m.id = pd.id_miasta AND pd.id_stan_pogody = s.id AND date(pd.data) = date('now');








SELECT DISTINCT m.nazwa_miasta FROM miasto as m, Miasto_Uzytkownika as mu
WHERE m.id = mu.id_miasta ;
SELECT pd.min_temp, pd.max_temp, s.stan_pogody FROM pogoda_dzienna AS pd, stanpogody AS s, miasto AS m
WHERE pd.id_stan_pogody = s.id AND pd.id_miasta = m.id AND date(pd.data) = date('now') AND m.nazwa_miasta = 'Rzeszów';
SELECT m.id AS id_miasta, u.email, u.username  FROM Miasto_Uzytkownika AS mu, user AS u, miasto AS m
WHERE u.id = mu.id_uzytkownika AND m.id = mu.id_miasta AND m.nazwa_miasta = 'Rzeszów';

