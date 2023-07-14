from moviepy.editor import VideoFileClip, vfx
from os.path import splitext


def load_video(video: str | VideoFileClip) -> VideoFileClip:
    if isinstance(video, VideoFileClip):
        return video
    return VideoFileClip(video)


def change_duration(
    video: str | VideoFileClip, target_duration_s: int
) -> VideoFileClip:
    clip = load_video(video)
    duration = clip.duration

    speed = duration / target_duration_s
    return clip.fx(vfx.speedx, speed)


def resize_mov(
    video: str | VideoFileClip, new_width: int, new_height: int
) -> VideoFileClip:
    video = load_video(video)
    return video.resize((new_width, new_height))


def save_mov(
    video: VideoFileClip,
    output_path: str,
    audio: bool = True,
    fps: int = 60,
    codec: str = "libx264",
) -> None:
    _, ext = splitext(output_path)
    if not ext:
        output_path += ".mov"
    video.write_videofile(output_path, audio=audio, fps=fps, codec=codec)


if __name__ == "__main__":
    video_path = "slow_movie.mov"
    output_path = "new_speed.mov"
    target_duration = 5
    new_width = 1080
    new_height = 1920

    faster_clip = change_duration(video_path, target_duration)
    faster_resized = resize_mov(faster_clip, new_width, new_height)
    save_mov(faster_resized, output_path, audio=False)
