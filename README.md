# ultrasonic-distance-visualizer
아두이노 초음파센서를 이용해 수집한 정보를 파이썬으로 처리(시각화)

## 주요 내용
- 초음파 센서로 거리 측정
- 아두이노 시리얼 통신
- 파이썬에서 실시간 데이터 수신
- matplotlib을 이용한 시각화
- 측정 실패값 필터링

## 사용 기술
- Arduino
- HC-SR04
- Python
  - pyserial
  - matplotlib

## 실행 방법
1. 아두이노에 ultrasonic_sensor.ino 업로드
2. 파이썬 패키지 설치
```bash
pip install pyserial matplotlib
```
3. main.py에서 포트 번호 수정(COM1,COM2 등등)
4. 파이썬 실행

## 확장 계획
여러 개의 초음파 센서를 배열하여 물체의 대략적인 윤곽을 추정하는 방식으로 확장 고려
