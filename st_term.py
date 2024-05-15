import speedtest
import time
from tqdm import tqdm

def display_speed():
    st = speedtest.Speedtest()
    with tqdm(total=2, desc="Running speed test", unit="test") as pbar:
        # Download test
        pbar.set_description("Downloading")
        st.download()
        pbar.update(1)

        # Upload test
        pbar.set_description("Uploading")
        st.upload()
        pbar.update(1)

        

    download_speed = st.results.download / 1024 / 1024  # Convert from bytes to megabits
    upload_speed = st.results.upload / 1024 / 1024  # Convert from bytes to megabits
    ping = st.results.ping

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {round(ping, 2)} ms")

def main():
    while True:
        display_speed()
        print("Waiting for the next test...")
        time.sleep(60)  # Wait for 60 seconds before running the next test

if __name__ == "__main__":
    main()
