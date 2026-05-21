from qiskit import QuantumCircuit, QuantumRegister
import matplotlib.pyplot as plt

# สร้าง Quantum Circuit
qc = QuantumCircuit()

# สร้าง Quantum Register ที่มี 2 คิวบิต
qr = QuantumRegister(2, 'qreg')
qc.add_register(qr)

# วาดวงจรและแสดงภาพ
qc.draw(output='mpl')

from pathlib import Path
plt.savefig(f'{Path(__file__).stem}.png') 
plt.close() 
