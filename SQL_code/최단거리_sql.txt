-- 확장 모듈을 추가
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS pgrouting;

--인덱싱 자료구조 설정 / 더 빠른 탐색 위함
--link의 경우 select column_name from information_schema.columns  where TABLE_NAME = 'moct_link'를 통해 컬럼명 확인후 진행 이때 오류발생시 건너뛰기(geom칼럼과 같이 데이터가 큰 경우 발생)
--node의 경우 select column_name from information_schema.columns  where TABLE_NAME = 'moct_node' 를 통해 컬럼명 확인
create index moctlink_gid_idx on public.moct_link(gid);
create index moctlink_lanes_idx on public.moct_link(lanes);
create index moctlink_max_spd_idx on public.moct_link(max_spd);
create index moctlink_rest_w_idx on public.moct_link(rest_w);
create index moctlink_rest_h_idx on public.moct_link(rest_h);
create index moctlink_length_idx on public.moct_link(length);
create index moctlink_road_no_idx on public.moct_link(road_no);
create index moctlink_road_name_idx on public.moct_link(road_name);
create index moctlink_road_use_idx on public.moct_link(road_use);
create index moctlink_multi_link_idx on public.moct_link(multi_link);
create index moctlink_connect_idx on public.moct_link(connect);
create index moctlink_remark_idx on public.moct_link(remark);
create index moctlink_link_id_idx on public.moct_link(link_id);
create index moctlink_f_node_idx on public.moct_link(f_node);
create index moctlink_t_node_idx on public.moct_link(t_node);
create index moctlink_rest_veh_idx on public.moct_link(rest_veh);
create index moctlink_road_rank_idx on public.moct_link(road_rank);
create index moctlink_road_type_idx on public.moct_link(road_type);

create index moctnode_gid_idx on public.moct_node(gid);
create index moctnode_geom_idx on public.moct_node(geom);
create index moctnode_node_type_idx on public.moct_node(node_type);
create index moctnode_turn_p_idx on public.moct_node(turn_p);
create index moctnode_remark_idx on public.moct_node(remark);
create index moctnode_node_name_idx on public.moct_node(node_name);
create index moctnode_node_id_idx on public.moct_node(node_id);

-- 기존 테이블 구조 확인
SELECT * FROM 천안시_관광업소_동;
SELECT * FROM 천안시_관광업소_서;
SELECT * FROM 숙박데이터_최종;
SELECT * FROM 천안시_빵소;

-- 테이블에 `geom` 칼럼 추가
--ALTER TABLE cheonan_bbangso_location ADD COLUMN geom GEOMETRY(Point, 4326);
--ALTER TABLE cheonan_tourist_attraction ADD COLUMN geom GEOMETRY(Point, 4326);
--ALTER TABLE 천안시_관광업소_동 ADD COLUMN geom GEOMETRY(Point, 4326);
--ALTER TABLE 천안시_관광업소_서 ADD COLUMN geom GEOMETRY(Point, 4326);
--ALTER TABLE 숙박데이터_최종 ADD COLUMN geom GEOMETRY(Point, 4326);
--ALTER table 천안시_빵소 ADD COLUMN geom GEOMETRY(Point, 4326);

-- 좌표 데이터로 `geom` 칼럼 업데이트
--UPDATE cheonan_bbangso_location 
--SET geom = ST_SetSRID(ST_Point(lon, lat), 4326);

--UPDATE cheonan_tourist_attraction 
--SET geom = ST_SetSRID(ST_Point(lon, lat), 4326);

--UPDATE 천안시_관광업소_동 
--SET geom = ST_SetSRID(ST_Point(lon, lat), 4326);

--UPDATE 천안시_관광업소_서 
--SET geom = ST_SetSRID(ST_Point(lon, lat), 4326);

--UPDATE 숙박데이터_최종 
--SET geom = ST_SetSRID(ST_Point(lon, lat), 4326);

-- `geom` 칼럼 추가 확인 / 확인 완
--SELECT * FROM cheonan_bbangso_location;
--SELECT * FROM cheonan_tourist_attraction;
--SELECT * FROM 천안시_관광업소_동;
--SELECT * FROM 천안시_관광업소_서;
--SELECT * FROM 숙박데이터_최종;
--SELECT * FROM 천안시_빵소;

-- min_cost 산정 및 인덱스 생성
-- min_cost란 도로 link의 경로를 통과할 때 최소시간 선정
-- length / (max_spd / 36) / 10, 링크의 길이를 해당 속도로 나눈 값, 링크를 최대 속도로 주행할 때 걸리는 시간 계산
ALTER TABLE moct_link ADD COLUMN min_cost real; -- mock_link 테이블 수정 및 min_cost란 열 추가 + 실수형데이터타입으로 생성
UPDATE moct_link SET min_cost = (length / (max_spd::real / 36) / 10); -- min_cost 열의 값을 덥데이트한다 속도를 변환 km/h -> m/s 변환
CREATE INDEX min_cost_idx ON public.moct_link(min_cost); -- creat index 생성할 인덱스 이름, on public.moct_link 인덱스를 생성할 테이블 지정

--검색
select l.f_node,l.geom from moct_link as l where l.road_name like '천안%';

-- 임시 테이블 `temp_points` 생성 및 데이터 삽입
DROP TABLE IF EXISTS temp_points;
-- 삭제 확인
SELECT * FROM temp_points;
CREATE TEMP TABLE temp_points (
    point_id SERIAL PRIMARY KEY, 
    geom GEOMETRY(Point, 4326)
);
-- 생성 확인
SELECT * FROM temp_points;

-- temp_points 테이블의 SRID 확인
SELECT DISTINCT ST_SRID(geom) FROM temp_points;

-- moct_node 테이블의 SRID 확인
SELECT DISTINCT ST_SRID(geom) FROM moct_node;

-- 임시 테이블에 시작점, 경유지, 끝점 좌표를 수동으로 입력
INSERT INTO temp_points (geom) VALUES 
    (ST_SetSRID(ST_Point(127.113046978689, 36.8161298541125), 4326)), -- 시작점 / 천안시청
    (ST_SetSRID(ST_Point(127.13181, 36.805138), 4326)), -- 경유지1 / 몽상가인
    (ST_SetSRID(ST_Point(127.15757, 36.815174), 4326)), -- 경유지2 / 시바앙과자
    (ST_SetSRID(ST_Point(127.2304, 36.78187), 4326)); -- 끝점 / 독립기념관

-- 좌표 데이터 삽입 확인
SELECT * FROM temp_points

-- 가장 가까운 노드 탐색
-- 임시 결과를 저장, ST_Distance 함수로 가장 가까운 노드 탐색
create table closest_node_result as
WITH closest_nodes AS (
    SELECT 
        tp.point_id, 
        n.node_id, 
        ST_Distance(tp.geom, ST_Transform(n.geom, 4326)) AS distance
    FROM 
        temp_points tp
    JOIN 
        moct_node n 
    ON 
        ST_Distance(tp.geom, ST_Transform(n.geom, 4326)) IS NOT NULL
    ORDER BY 
        tp.point_id, 
        distance
)
SELECT DISTINCT ON (point_id) 
    point_id, 
    node_id, 
    distance
FROM 
    closest_nodes
ORDER BY 
    point_id, 
    distance;

-- 좌표 최인근 노드 좌표가 삽입됐는지 확인
select * from closest_node_result;

-- `closest_node_result` 테이블에서 가져온 노드 ID를 사용하여 `pgr_dijkstraVia` 수행
-- 예를 들어 얻어진 노드 ID가 1 (시작점), 2 (경유지1), 3 (경유지2), 4 (끝점)일 경우
DROP TABLE IF EXISTS dijkstraVia_result;
CREATE TABLE dijkstraVia_result AS
SELECT
    l.road_name,
    l.max_spd,
    l.length,
    l.min_cost,
    l.geom,
    d.path_seq,
    d.agg_cost
FROM
    moct_link AS l
INNER JOIN (
    SELECT
        edge::varchar(10),
        seq,
        path_seq,
        node,
        cost,
        agg_cost
    FROM
        pgr_dijkstraVia(
            'SELECT link_id::bigint AS id,
                    f_node::bigint AS source,
                    t_node::bigint AS target,
                    length::bigint AS cost
             FROM moct_link',
    		ARRAY[ 
        (SELECT node_id::bigint FROM closest_node_result WHERE point_id = 1),
        (SELECT node_id::bigint FROM closest_node_result WHERE point_id = 2),
        (SELECT node_id::bigint FROM closest_node_result WHERE point_id = 3),
        (SELECT node_id::bigint FROM closest_node_result WHERE point_id = 4)
    ]
        )
) AS d
ON
    l.link_id = d.edge;

-- 최단경로에 해당되는 도로 정보, 경로의 순서, 누적비용 계산
select *  from dijkstraVia_result;

-- 주행 경로 테이블 확인
SELECT * FROM dijkstraVia_result ORDER BY path_seq ASC;

-- 총 거리 계산
-- 도로 길이 / 해당 구간 최대 속도 
SELECT SUM(length / (max_spd * 1000 / 60)) AS "cost(minute)"FROM dijkstraVia_result;
