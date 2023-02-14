# Log Book

## Notable Obstacles

Video Codecs
- Struggled to keep Video Codecs consistent, it slows down the CLI prototype significantly.
- Does not matter what container the video is in.

Noise Parameters
- Difficult to find the right threshold of noise to make it visibly graining, or make image not too noisy.
- Need to find a way to search for all and experiment all parameters.

Implementing "Realistic Film Grain"
- Implementation based from C++ implementation and is very difficult to understand
- Just need to read more and understand it, ask for external help

Unknown error "mmco: unref short failure"
- Not sure how to fix, it does not affect the editor as I know
- But it needs to be fix so that printing in terminal is cleaning, error-free

Limited number of layers to images
- Because Tkinter is difficult to make scrollable frames to allow for multiple layers
- Current Solution is to limit number of layers it can have (5 at the moment)

Playing Videos within the Editor
- Very difficult to have images change every framestep in the editor, usually crashes the editor
- Potential Solution could be to switch between TkVideoPlayer/ and Image after pressing play

Performance Drops on High Res Images
- Unsure how to overcome this at the moment, only affected when adding Film Grain


## References

More Modern CustomTkinter GUI Tutorial
- Available at: [Medium](https://medium.com/@fareedkhandev/modern-gui-using-tkinter-12da0b983e22)
