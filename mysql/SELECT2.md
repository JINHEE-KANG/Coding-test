# 역순 정렬하기
### 출처
프로그래머스>코딩테스트 연습>SQL 고득점 KIT>SELECT>역순 정렬하기
[문제 보러 가기](https://programmers.co.kr/learn/courses/30/lessons/59036)

### 문제 설명

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| INTAKE_CONDITION | VARCHAR(N) | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |

동물 보호소에 들어온 모든 동물의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 ANIMAL_ID 역순으로 보여주세요. SQL을 실행하면 다음과 같이 출력되어야 합니다.

### 결과 예시

| NAME   | DATETIME            |
| ------ | ------------------- |
| Rocky  | 2016-06-07 09:17:00 |
| Shelly | 2015-01-29 15:01:00 |
| Benji  | 2016-04-19 13:28:00 |
| Jackie | 2016-01-03 16:25:00 |
| *Sam   | 2016-03-13 11:17:00 |

..이하 생략

------

본 문제는 [Kaggle의 Austin Animal Center Shelter Intakes and Outcomes](https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes)에서 제공하는 데이터를 사용하였으며 [ODbL](https://opendatacommons.org/licenses/odbl/1.0/)의 적용을 받습니다.



### CODE

```mysql
-- 코드를 입력하세요
SELECT `NAME`,`DATETIME`
FROM `ANIMAL_INS`
ORDER BY `ANIMAL_ID` DESC;
```



### RESULT

| NAME         | DATETIME          |
| ------------ | ----------------- |
| Rocky        | 2016-06-07  9:17  |
| Shelly       | 2015-01-29  15:01 |
| Benji        | 2016-04-19  13:28 |
| Jackie       | 2016-01-03  16:25 |
| *Sam         | 2016-03-13  11:17 |
| Jimminee     | 2015-07-28  18:17 |
| Mitty        | 2014-06-21  12:25 |
| Raven        | 2015-11-19  13:41 |
| Chewy        | 2016-09-11  14:09 |
| Stanley      | 2016-04-02  11:36 |
| Lizzie       | 2014-12-25  12:02 |
| Jake         | 2016-10-18  11:01 |
| Sabrina      | 2016-05-12  20:23 |
| Kaila        | 2014-05-16  14:17 |
| Anna         | 2013-11-18  17:03 |
| Lucy         | 2017-06-17  13:29 |
| Reggie       | 2016-10-04  20:31 |
| Jack         | 2013-10-14  15:38 |
| Lucy         | 2015-08-25  14:08 |
| Charlie      | 2017-07-12  14:43 |
| Raven        | 2016-08-22  16:13 |
| Rogan        | 2015-12-27  17:42 |
| Snickerdoodl | 2015-01-24  16:14 |
| Chip         | 2015-07-26  11:39 |
| Skips        | 2013-11-20  13:09 |
| Penny        | 2014-01-31  13:46 |
| Nellie       | 2017-03-16  16:53 |
| Rome         | 2016-04-06  15:53 |
| Holly        | 2013-12-08  17:04 |
| Blaze        | 2015-11-27  15:59 |
| Spider       | 2015-12-25  10:13 |
| Dakota       | 2014-06-25  16:58 |
| Goldie       | 2014-02-01  18:36 |
| Punch        | 2015-08-17  12:55 |
| Tiko         | 2015-12-19  12:52 |
| Giovanni     | 2015-09-25  18:17 |
| Clyde        | 2014-01-11  15:15 |
| Jedi         | 2014-12-13  15:19 |
| Jj           | 2014-07-04  1:55  |
| Finney       | 2017-02-05  12:27 |
| Oreo         | 2014-05-29  12:31 |
| Princess     | 2014-11-08  16:14 |
| Maxwell  2   | 2015-03-13  13:14 |
| Cherokee     | 2017-07-08  9:41  |
| Pepper       | 2014-08-06  12:07 |
| Ruby         | 2016-01-22  17:13 |
| Laika        | 2017-08-04  16:45 |
| Scooby       | 2014-02-03  12:41 |
| Pickle       | 2016-02-01  14:35 |
| Disciple     | 2013-10-23  11:42 |
| Mercedes     | 2017-09-28  13:36 |
| Zoe          | 2014-07-05  7:13  |
| Lyla         | 2014-08-02  11:23 |
| Frijolito    | 2014-01-25  14:38 |
| Lucy         | 2017-10-25  17:17 |
| Dora         | 2017-07-09  7:42  |
| Mama  Dog    | 2014-02-18  12:24 |
| Dash         | 2015-06-12  12:47 |
| Rosie        | 2014-03-20  12:31 |
| Ella         | 2014-07-29  11:43 |
| April        | 2016-06-07  17:42 |
| Sailor       | 2015-05-11  12:33 |
| Ceballo      | 2015-08-03  9:09  |
| Greg         | 2015-07-29  16:07 |
| Katie        | 2013-11-03  15:04 |
| Emily        | 2014-10-27  14:43 |
| Sniket       | 2016-06-25  11:46 |
