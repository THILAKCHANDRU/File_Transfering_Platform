import socket

# Define server host and port
HOST = '192.168.248.86'  # Update to server IP if running on a different machine
PORT = 8000

def request_video(video_name, save_path):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        
        # Send request for the video file
        client_socket.sendall(video_name.encode())
        
        # Open the file to write the received data
        with open(save_path, 'wb') as video_file:
            while True:
                data = client_socket.recv(1024)  # Receive 1024 bytes at a time
                if b"ERROR:" in data:
                    print(data.decode())  # Display error message if file not found
                    break
                elif data == b"EOF":  # End of file received
                    print("File transfer complete!")  # Notify the client about completion
                    break
                video_file.write(data)
        
        print(f"Video saved as {save_path}")  # Notify where the file was saved
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()  # Close the connection after receiving the file

if __name__ == "__main__":
    video_to_request = input("Enter the file name with extension: ")  # Request the video by name
    save_location = "received_video.mp4"  # Save the received video with this name
    request_video(video_to_request, save_location)
