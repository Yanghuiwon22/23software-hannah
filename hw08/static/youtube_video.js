<!DOCTYPE html>
<html>
<head>
    <title>YouTube API 예제</title>
</head>
<body>
    <h1>YouTube API 예제</h1>
    <div id="player"></div>

    <script src="https://www.youtube.com/iframe_api"></script>
    <script>
        // YouTube API를 비동기로 로드
        var tag = document.createElement('script');
        tag.src = 'https://www.youtube.com/iframe_api';
        var firstScriptTag = document.getElementsByTagName('script')[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

        var player;
        function onYouTubeIframeAPIReady() {
            player = new YT.Player('player', {
                height: '360',
                width: '640',
                videoId: '동영상_ID',
                playerVars: {
                    controls: 1,
                    showinfo: 0,
                    rel: 0,
                },
                events: {
                    'onReady': onPlayerReady,
                }
            });
        }

        function onPlayerReady(event) {
            event.target.playVideo();
        }
    </script>
</body>
</html>