<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?font=Roboto&weight=700&size=35&pause=1000&color=34ebc2&center=true&vCenter=true&width=600&lines=Bodha+AI;Real-Time+Mental+Wellness+Companion;Voice+%26+Text+Interaction;Powered+by+LiveKit+%26+LLMs;Active+Experimental+Prototype" alt="Typing SVG" />
</div>

<div align="center">
  <img src="https://img.shields.io/badge/Status-Active%20Prototype-2ea44f?style=for-the-badge" alt="Status Active" />
  <img src="https://img.shields.io/badge/Real--Time-LiveKit-purple?style=for-the-badge&logo=livekit" alt="LiveKit" />
  <img src="https://img.shields.io/badge/Focus-Wellness%20%26%20Reflection-34ebc2?style=for-the-badge" alt="Focus Wellness" />
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
</div>

<br />

<div align="center">
  <h3>🧠 Project Evolution: MindCare+ ➡️ Bodha AI</h3>
  <p>
    <b>Bodha AI</b> represents a generational leap from its predecessor, <i>MindCare+</i>. While the original focused on text-based therapy assistance, Bodha AI introduces <b>multimodal interaction (Voice + Text)</b> powered by real-time streaming technology to create a more grounded, human-like presence for emotional self-reflection.
  </p>
</div>

---

```mermaid
graph TD
    User([👤 User]) -->|Microphone Input| FE[💻 Frontend / Client]
    FE -->|WebRTC Stream| LK[📡 LiveKit Server]
    
    subgraph "Backend Agent"
    LK <-->|Audio Packet| AG[🤖 Python Agent]
    AG -->|Audio Stream| VAD[🔈 Voice Activity Detection]
    VAD -->|User Speech| STT[📝 STT Model]
    STT -->|Transcribed Text| LLM[🧠 LLM Reasoning Engine]
    LLM -->|Response Text| TTS[🗣️ TTS Model]
    TTS -->|Synthesized Audio| AG
    end
    
    AG -->|Response Audio| LK
    LK -->|Playback| FE
    FE -->|Audio Output| User
