-- uses hbtn_0d_tv_shows to list all genres not linked to the show Dexter
SELECT name FROM tv_genres
WHERE id NOT IN (
	SELECT tv_genres.id FROM tv_genres
	JOIN tv_show_genres ON id=tv_show_genres.genre_id
	JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
	WHERE tv_shows.title="Dexter"
)
ORDER BY name;
