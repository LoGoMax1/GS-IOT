import cv2
import mediapipe as mp

# Inicializa o MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Captura da webcam
cap = cv2.VideoCapture(0)

# Índices dos dedos
finger_names = ["Polegar", "Indicador", "Médio", "Anelar", "Mínimo"]
finger_tips = [4, 8, 12, 16, 20]
finger_pips = [2, 6, 10, 14, 18]

while True:
    success, frame = cap.read()
    if not success:
        print("Erro ao acessar a webcam.")
        break

    frame = cv2.flip(frame, 1)  # Espelha a imagem
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            dedos_abax = []
            for i in range(5):
                tip_y = hand_landmarks.landmark[finger_tips[i]].y
                pip_y = hand_landmarks.landmark[finger_pips[i]].y
                estado = tip_y > pip_y  # True se abaixado
                dedos_abax.append(estado)

            # Detectar gesto de alerta:
            # Condições:
            # - Polegar está dobrado (abaixo da base do indicador)
            # - Os 4 dedos restantes estão abaixados
            polegar_dobrado = hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x  # Dobrado para dentro
            dedos_fechando = all(dedos_abax[1:])  # Indicador ao mínimo abaixados

            if polegar_dobrado and dedos_fechando:
                cv2.putText(frame, "SINAL DE PEDIDO DE AJUDA DETECTADO ⚠", (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 3)

    cv2.imshow("Detecção de Gesto de Socorro", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
