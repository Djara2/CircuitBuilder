class BinaryLogic:
    GATES = {"AND", "OR", "XOR", "NOT", "NAND", "NOR"}

    def AND(values: list) -> int:
        boolean_result: bool = all(values)
        result: int = 1 if boolean_result == True else 0
        return(result)
    
    def OR(values: list) -> int:
        boolean_result: bool = any(values) 
        result: int = 1 if boolean_result == True else 0
        return(result)
    
    def XOR(values: list) -> int:
        # XOR is true when an odd number of inputs are high
        high_inputs: list = [value for value in values if value == 1]
        cardinality: int = len(high_inputs)
        result: int = 1 if cardinality % 2 != 0 else 0
        return(result)
    
    def NOT(value: int) -> int:
        if type(value) == list:
            value = value[0]

        result: int = 0 if value == 1 else 1
        return(result)

    def NAND(values: list) -> int:
        return(NOT(AND(values)))
    
    def NOR(values: list) -> int:
        return(NOT(OR(values)))

class Line:
    def __init__(self, name: str, value: int, trace = []):
        self.name = name
        self.value = value
        # keeps track of how the line's value changes
        # after being passed through gates
        self.trace = trace
        if trace == []:
            self.trace = [self.value]
        self.trace_length = len(self.trace)

    def set(self, value: int) -> None:
        self.value = value
        self.trace[self.trace_length - 1] = value

    def new_signal(self, value) -> None:
        self.value = value
        self.trace.append(value)
        self.trace_length += 1

    def __str__(self) -> str:
        return(f"{self.name}: {self.value}")

class Gate:
    def __init__(self, type: str, sources = []): 
        self.type = type
        self.sources = sources # list of lines

    def evaluate(self) -> int:
        if not self.type in BinaryLogic.GATES:
            return(-1)
        
        signals = [source.trace[source.trace_length - 1] for source in self.sources]

        if self.type == "AND":
            result = BinaryLogic.AND(signals)

        elif self.type == "OR":
            result == BinaryLogic.OR(signals)

        elif self.type == "XOR":
            result = BinaryLogic.XOR(signals)

        elif self.type == "NOT":
            result = BinaryLogic.NOT(signals)

        elif self.type == "NAND":
            result = BinaryLogic.NAND(signals)

        elif self.type == "NOR":
            result = BinaryLogic.NOR(signals)

        else:
            result = -1

        return(result)
    
    def __str__(self) -> str:
        inputs = [str(line) for line in self.sources]
        value = self.evaluate()
        string = f"{self.type} gate with inputs {inputs} -> {value}"
        return(string)
