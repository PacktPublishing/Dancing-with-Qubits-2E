# Construct a circuit from a byte using Cirq
import cirq

circuit = cirq.Circuit()
qubits = cirq.LineQubit.range(8)

def build_circuit_from_byte(byte):
    # Iterate at most 8 times over the input
    for n in reversed(range(8)):
        if byte % 2:
            # Insert an X gate to get |1>
            circuit.append(cirq.X(qubits[n]))
        else:
            # Insert an identity gate to keep |0>
            circuit.append(cirq.I(qubits[n]))
        byte //= 2

build_circuit_from_byte(0b01101011)

print(circuit)

def Lp(v, p):
  assert isinstance(v, list) and isinstance(p, int) and p > 0
  sum = 0
  for entry in v:
    sum += pow(abs(entry), p)
  return pow(sum, 1/p)

v = [3,7]
Lp(v, 2)

for p in [1, 2, 10, 25, 50, 100]:
    print(f"{p}: {Lp(v, p)}")

