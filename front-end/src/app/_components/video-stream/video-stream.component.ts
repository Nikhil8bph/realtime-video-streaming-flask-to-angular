import { Component } from '@angular/core';
import { Socket } from 'ngx-socket-io';

@Component({
  selector: 'app-video-stream',
  templateUrl: './video-stream.component.html',
  styleUrls: ['./video-stream.component.css']
})
export class VideoStreamComponent {
  videoStream: string;

  constructor(private socket: Socket) {}

  ngOnInit(): void {
    this.socket.on('video_stream', (base64Image: string) => {
      this.videoStream = 'data:image/jpeg;base64,' + base64Image;
    });
  }
}
