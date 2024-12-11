-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Get the crime description from crime_scene_reports table
SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND year = 2023 And street = 'Humphrey Street';

-- Theft happened at around 10:15am at the bakery
SELECT * FROM bakery_security_logs WHERE day = 28 AND hour = 10 AND minute >= 15;

-- Interview 1: Thief left parking lot ~10 minutes after the theft
    -- Suspicious plates: 94KL13X, 322W7JE, 1106N58
    SELECT * FROM people WHERE license_plate IN
    (SELECT license_plate FROM bakery_security_logs WHERE day = 28 AND hour = 10 AND minute >= 15 AND activity = 'exit');

-- Interview 2: Thief withdrew money from Leggett Street atm earlier that morning
SELECT * FROM atm_transactions WHERE month = 7 AND day = 28 AND atm_location = 'Leggett Street';
    -- Suspicious account numbers: 76054385, 49610011, 26013199

-- Interview 3: As thief was leaving, phone call happened for less than a minute, earliest flight the next day, ticket purcase
SELECT * FROM phone_calls WHERE day = 28 AND month = 7 AND duration <= 60
AND caller = '(286) 555-6063';
    -- Suspicious callers: (367) 555-5533, (286) 555-6063
    -- Suspicious accomplices: (375) 555-8161, (676) 555-6554, (725) 555-3243


-- SUSPICIOUS PEOPLE ID:
--      449774 - Taylor called (676) 555-6554
--      686048 - Bruce called (375) 555-8161

-- SUSPICOUS ACCOMPLICE ID:
--      250277
--      847116
--      864400

-- Get the people with suspicious phone number and license plate
SELECT * FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
WHERE license_plate IN
(SELECT license_plate FROM bakery_security_logs WHERE day = 28 AND hour = 10 AND minute >= 15 AND activity = 'exit')
AND phone_number IN
(SELECT caller FROM phone_calls WHERE day = 28 AND month = 7 AND duration <= 60);


-- Get the people that could be accomplice based on phone numbers
SELECT * FROM people WHERE phone_number = '(375) 555-8161' OR phone_number = '(676) 555-6554' OR phone_number = '(725) 555-3243';

-- Get the earliest flight departing from Fiftyville on 7/29
SELECT * FROM flights WHERE origin_airport_id = 8 AND month = 7 AND day = 29 ORDER BY hour;

    --Flight id = 36, destination airport id = 4

-- Get what the destination is
SELECT * FROM airports WHERE id = 4;
    -- Destination is LaGuardia

SELECT * FROM people WHERE passport_number IN
(SELECT passport_number FROM passengers WHERE flight_id = 36)
AND phone_number IN
(SELECT phone_number FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
WHERE license_plate IN
(SELECT license_plate FROM bakery_security_logs WHERE day = 28 AND hour = 10 AND minute >= 15 AND activity = 'exit')
AND phone_number IN
(SELECT caller FROM phone_calls WHERE day = 28 AND month = 7 AND duration <= 60));


-- Get phone numbers of potential accomplices
SELECT * FROM phone_calls WHERE month = 7 AND day = 28 AND duration <= 60 AND (caller = '(286) 555-6063' OR caller = '(367) 555-5533');


-- Get potential accomplices
SELECT * FROM people WHERE phone_number IN
(SELECT receiver FROM phone_calls WHERE month = 7 AND day = 28 AND duration <= 60 AND (caller = '(286) 555-6063' OR caller = '(367) 555-5533'));


SELECT phone_number FROM people WHERE phone_number IN
(SELECT receiver FROM phone_calls WHERE month = 7 AND day = 28 AND duration <= 60 AND (caller = '(286) 555-6063' OR caller = '(367) 555-5533'));

SELECT * FROM people WHERE passport_number IN
(SELECT passport_number FROM passengers WHERE flight_id = 36)
AND phone_number IN
(SELECT phone_number FROM people WHERE phone_number IN
(SELECT receiver FROM phone_calls WHERE month = 7 AND day = 28 AND duration <= 60 AND (caller = '(286) 555-6063' OR caller = '(367) 555-5533')));
