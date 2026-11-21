from core.proof_engine import RuntimeProofEngine

class AgentRuntimeInterceptor:
    """
    Enforces runtime governance rules and validates MCP tool calls 
    before state transitions occur.
    """
    def __init__(self):
        self.proof_engine = RuntimeProofEngine()
        self.audit_logs = []

    def intercept_mcp_call(self, agent_id, tool_name, parameters):
        if not parameters:
            raise ValueError("Execution halted: Empty parameters passed to MCP server.")
        
        # Generate cryptographic proof for the execution step
        proof = self.proof_engine.generate_proof(agent_id, f"CALL_TOOL_{tool_name}", parameters)
        self.audit_logs.append(proof)
        
        return {
            "status": "APPROVED_AND_LOGGED",
            "proof": proof
        }
