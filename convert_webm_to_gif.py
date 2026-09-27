import os
import imageio

def convert():
    input_path = "/config/Desktop/Session1/simple-agent/assets/demo_agent.webm"
    output_path = "/config/Desktop/Session1/simple-agent/assets/demo.gif"
    root_output_path = "/config/Desktop/Session1/assets/demo.gif"

    print(f"Reading video from {input_path}...")
    reader = imageio.get_reader(input_path)
    fps = reader.get_meta_data().get("fps", 10)
    print(f"Video FPS: {fps}")

    writer = imageio.get_writer(output_path, fps=min(fps, 10), loop=0)
    root_writer = imageio.get_writer(root_output_path, fps=min(fps, 10), loop=0)

    # Subsample frames to optimize GIF size (every 2nd frame)
    for i, frame in enumerate(reader):
        if i % 2 == 0:
            writer.append_data(frame)
            root_writer.append_data(frame)

    writer.close()
    root_writer.close()
    print(f"GIF saved at {output_path} and {root_output_path}")

if __name__ == "__main__":
    convert()
