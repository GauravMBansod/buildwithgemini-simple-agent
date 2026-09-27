import imageio.v3 as iio
from PIL import Image

def main():
    input_path = "/config/Desktop/Session1/simple-agent/assets/demo_agent.webm"
    output_path = "/config/Desktop/Session1/simple-agent/assets/demo.gif"
    root_output_path = "/config/Desktop/Session1/assets/demo.gif"

    print("Reading video frames...")
    frames = iio.imread(input_path, plugin="pyav") if hasattr(iio, "imread") else iio.imread(input_path)
    print(f"Total frames: {len(frames)}")

    pil_frames = []
    # Subsample frames (every 3rd frame) and resize to 640 width to make GIF lightweight and fast
    for frame in frames[::3]:
        img = Image.fromarray(frame)
        img.thumbnail((640, 400), Image.Resampling.LANCZOS)
        pil_frames.append(img)

    print(f"Saving {len(pil_frames)} frames to GIF...")
    if pil_frames:
        pil_frames[0].save(
            output_path,
            save_all=True,
            append_images=pil_frames[1:],
            optimize=True,
            duration=120,
            loop=0
        )
        pil_frames[0].save(
            root_output_path,
            save_all=True,
            append_images=pil_frames[1:],
            optimize=True,
            duration=120,
            loop=0
        )
        print("GIF conversion finished successfully!")

if __name__ == "__main__":
    main()
