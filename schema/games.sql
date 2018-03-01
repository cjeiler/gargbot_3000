DROP TABLE IF EXISTS games;
CREATE TABLE games (
game_id mediumint(8) unsigned NOT NULL PRIMARY KEY AUTO_INCREMENT,
name CHAR(50),
url CHAR(255) DEFAULT '',
pic_url CHAR(255) DEFAULT ''
);

DROP TABLE IF EXISTS games_votes;
CREATE TABLE games_votes (
game_id mediumint(8) ,
slack_id CHAR(9)
);
ALTER TABLE games_votes ADD CONSTRAINT constraintname UNIQUE (game_id, slack_id);

DROP TABLE IF EXISTS games_stars;
CREATE TABLE games_stars (
game_id mediumint(8) ,
slack_id CHAR(9)
);
ALTER TABLE games_stars ADD CONSTRAINT constraintname UNIQUE (game_id, slack_id);