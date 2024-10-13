import time

DELAY = 0.1

class Sender:
    def __init__(self, window_size, total_frames):
        self.window_size = window_size
        self.total_frames = total_frames
        self.base = 0
        self.next_seq_num = 0

    def send_frame(self, frame_num):
        print(f"Sending frame {frame_num}...")
        time.sleep(DELAY)

    def send_frames_in_window(self):
        print(f"Current Window: [{self.base} - {min(self.base + self.window_size - 1, self.total_frames - 1)}]")
        for frame_num in range(self.base, min(self.base + self.window_size, self.total_frames)):
            self.send_frame(frame_num)
        
    def send_frames(self):
        print("Sender:")
        while self.base < self.total_frames:
            self.send_frames_in_window()

            ack = input(f"Received ack for frame {self.base}? (y/n): ").strip().lower()
            if ack == 'y':
                print(f"Receiver: Acknowledgment received for frame {self.base}")
                self.base += 1
                if self.base < self.total_frames:
                   print(f"Updated base to {self.base}\n")
                else:
                    continue
                if self.base + self.window_size - 1 < self.total_frames:
                   print(f"Sending frame: {self.base + self.window_size - 1}")
                else:
                    continue
            elif ack == 'n':
                print("No acknowledgment received. Retransmitting the window...\n")
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def start(self):
        self.send_frames()

def main():
    total_frames = int(input("Enter total number of frames: "))
    window_size = int(input("Enter window size: "))

    sender = Sender(window_size, total_frames + 1)
    sender.start()

if __name__ == "__main__":
    main()
