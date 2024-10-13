
class SelectiveRepeatSender:
    def __init__(self, window_size, total_frames):
        self.window_size = window_size
        self.total_frames = total_frames
        self.base = 0
        self.next_seq_num = 0
        self.frames_in_transit = []

    def send(self):
        print("Sender:")
        while self.base < self.total_frames:
            print(f"Current Window: [{self.base}, {min(self.base + self.window_size - 1, self.total_frames - 1)}]")
            while self.next_seq_num < self.total_frames and self.next_seq_num < self.base + self.window_size:
                print("Sending frame ", self.next_seq_num,"...")
                self.frames_in_transit.append(self.next_seq_num)
                self.next_seq_num += 1

            self.receive_acknowledgment()

    def receive_acknowledgment(self):
        ack = input(f"Received ack for frame {self.base}? (y/n): ")
        print()
        if ack == 'y':
            print(f"Receiver: Acknowledgment received for frame {self.base}.")
            self.base += 1
            self.frames_in_transit.pop(0)
            print(f"Updated base to {self.base}\n")
        else:
            print(f"Receiver: Negative acknowledgment for frame {self.base}. \nRetransmitting...\n")

class SelectiveRepeatReceiver:
    def __init__(self, window_size, total_frames):
        self.window_size = window_size
        self.total_frames = total_frames
        self.expected_frame = 0

    def receive(self):
        print("Receiver:")
        while self.expected_frame < self.total_frames:
            print(f"Expecting frame: {self.expected_frame}")
            frame = self.expected_frame
            print("Receiver: Frame", frame, "received. Acknowledgment is sent.")
            self.expected_frame += 1
            print()

def main():
    total_frames = int(input("Enter total number of frames: "))
    window_size = int(input("Enter window size: "))

    sender = SelectiveRepeatSender(window_size, total_frames + 1)
    receiver = SelectiveRepeatReceiver(window_size, total_frames + 1)

    sender.send()
    receiver.receive()

if __name__ == "__main__":
    main()
