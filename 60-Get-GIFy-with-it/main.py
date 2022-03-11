from moviepy.editor import *

# Get GIFy with it

# Have the programme convert small video files into GIFs. Have a look at: http://zulko.github.io/blog/2014/01/23/making-animated-gifs-from-video-files-with-python/ for a tutorial.

#
# DISCLAIMER - I could not get moviepy to work on replit, so in order to run this program, you need to download and execute this locally.
#

class GIF:

    @staticmethod
    def gif():
        clip = (VideoFileClip('jomatech.mp4')
                .subclip((2, 4.5), (2, 5.5))
                .resize(0.5))

        clip.write_gif('wtf.gif')

    @staticmethod
    def gifFreezeRegion():
        clip = (VideoFileClip('jomatech.mp4')
                .subclip((2, 14), (2, 18))
                .resize(0.5))

        snapshot = (clip.crop(x2=clip.w/2)
                    .to_ImageClip(0.5)
                    .set_duration(clip.duration))

        composition = CompositeVideoClip([clip, snapshot])
        composition.write_gif('donut.gif', fps=15)

    @staticmethod
    def gifTimeSymmetrical():
        clip = (VideoFileClip('jomatech.mp4')
                .subclip((0, 23), (0, 25))
                .resize(0.5)
                .fx(lambda x: concatenate([x, x.fx(vfx.time_mirror)])))

        clip.write_gif('idea.gif')

    @staticmethod
    def gifWithText():
        clip = (VideoFileClip('jomatech.mp4')
                .subclip((0, 20), (0, 22))
                .resize(0.5))

        text = (TextClip('*Complex Maths*\nDo Not Disturb', fontsize=30, color='white')
                .set_pos((clip.w / 2 - 100, clip.h - 100))
                .set_duration(clip.duration))

        composite = CompositeVideoClip([clip, text])
        composite.write_gif('maths.gif', fps=10)


if __name__ == '__main__':
    GIF.gif()
