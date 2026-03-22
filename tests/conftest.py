"""
Pytest Configuration and Fixtures for Automotive Claude Code Agents

This module provides comprehensive fixtures for testing all aspects of
the automotive software development platform including skills, agents,
tools, workflows, and LLM council operations.
"""

import asyncio
import json
import os
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional
from unittest.mock import AsyncMock, MagicMock, Mock

import pytest
import yaml


# ============================================================================
# Session and Module Fixtures
# ============================================================================

@pytest.fixture(scope="session")
def project_root() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent.resolve()


@pytest.fixture(scope="session")
def skills_dir(project_root: Path) -> Path:
    """Get the skills directory."""
    return project_root / "skills"


@pytest.fixture(scope="session")
def agents_dir(project_root: Path) -> Path:
    """Get the agents directory."""
    return project_root / "agents"


@pytest.fixture(scope="session")
def workflows_dir(project_root: Path) -> Path:
    """Get the workflows directory."""
    return project_root / "workflows"


@pytest.fixture(scope="session")
def rules_dir(project_root: Path) -> Path:
    """Get the rules directory."""
    return project_root / "rules"


@pytest.fixture(scope="session")
def hooks_dir(project_root: Path) -> Path:
    """Get the hooks directory."""
    return project_root / "hooks"


@pytest.fixture(scope="session")
def tools_dir(project_root: Path) -> Path:
    """Get the tools directory."""
    return project_root / "tools"


# ============================================================================
# Temporary Directory Fixtures
# ============================================================================

@pytest.fixture
def temp_dir() -> Path:
    """Create a temporary directory for test artifacts."""
    temp_path = Path(tempfile.mkdtemp(prefix="automotive-test-"))
    yield temp_path
    shutil.rmtree(temp_path, ignore_errors=True)


@pytest.fixture
def temp_workspace(temp_dir: Path) -> Path:
    """Create a temporary workspace with ECU project structure."""
    workspace = temp_dir / "workspace"
    workspace.mkdir()

    # Create typical ECU project structure
    (workspace / "src").mkdir()
    (workspace / "include").mkdir()
    (workspace / "config").mkdir()
    (workspace / "tests").mkdir()
    (workspace / "docs").mkdir()
    (workspace / "build").mkdir()

    # Create sample files
    (workspace / "src" / "main.c").write_text(
        "int main(void) {\n    return 0;\n}\n"
    )
    (workspace / "include" / "config.h").write_text(
        "#ifndef CONFIG_H\n#define CONFIG_H\n#endif\n"
    )

    return workspace


@pytest.fixture
def temp_autosar_project(temp_dir: Path) -> Path:
    """Create a temporary AUTOSAR project structure."""
    project = temp_dir / "autosar-project"
    project.mkdir()

    # AUTOSAR directory structure
    (project / "config" / "Rte").mkdir(parents=True)
    (project / "config" / "Os").mkdir(parents=True)
    (project / "config" / "EcuC").mkdir(parents=True)
    (project / "generation").mkdir()
    (project / "src" / "application").mkdir(parents=True)
    (project / "src" / "bsw").mkdir(parents=True)

    # Sample AUTOSAR files
    (project / "config" / "EcuC" / "EcuC.arxml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<AUTOSAR></AUTOSAR>\n'
    )

    return project


# ============================================================================
# Automotive Data Fixtures
# ============================================================================

@pytest.fixture
def sample_can_dbc() -> str:
    """Sample CAN DBC file content."""
    return """VERSION ""

NS_ :
    NS_DESC_
    CM_
    BA_DEF_
    BA_
    VAL_

BS_:

BO_ 256 BMS_Status: 8 BMS
 SG_ Battery_Voltage : 0|16@1+ (0.01,0) [0|655.35] "V" VCU
 SG_ Battery_Current : 16|16@1- (0.1,-3276.8) [-3276.8|3276.7] "A" VCU
 SG_ SOC : 32|8@1+ (0.5,0) [0|100] "%" VCU
 SG_ Temperature : 40|8@1- (1,-40) [-40|215] "degC" VCU

BO_ 512 VCU_Command: 8 VCU
 SG_ Charge_Enable : 0|1@1+ (1,0) [0|1] "" BMS
 SG_ Discharge_Enable : 1|1@1+ (1,0) [0|1] "" BMS
 SG_ Max_Charge_Current : 8|16@1+ (0.1,0) [0|400] "A" BMS
 SG_ Max_Discharge_Current : 24|16@1+ (0.1,0) [0|400] "A" BMS
"""


@pytest.fixture
def sample_ecu_config() -> Dict[str, Any]:
    """Sample ECU configuration."""
    return {
        "ecu_name": "BMS_Master",
        "ecu_type": "Battery Management System",
        "mcu": {
            "family": "STM32F4",
            "part": "STM32F407VGT6",
            "clock_mhz": 168,
            "flash_kb": 1024,
            "ram_kb": 192
        },
        "communication": {
            "can": [
                {"interface": "CAN1", "baudrate": 500000, "role": "master"},
                {"interface": "CAN2", "baudrate": 250000, "role": "slave"}
            ],
            "uart": [
                {"interface": "USART1", "baudrate": 115200, "purpose": "debug"}
            ],
            "i2c": [
                {"interface": "I2C1", "speed": 400000, "devices": ["EEPROM"]}
            ]
        },
        "safety": {
            "asil_level": "ASIL-D",
            "iso26262_compliant": True,
            "watchdog_timeout_ms": 100
        }
    }


@pytest.fixture
def sample_bms_requirements() -> List[Dict[str, Any]]:
    """Sample BMS requirements."""
    return [
        {
            "id": "REQ-BMS-001",
            "title": "Cell voltage monitoring",
            "description": "System shall monitor all cell voltages with 10mV accuracy",
            "category": "Safety",
            "asil": "D",
            "priority": "Critical"
        },
        {
            "id": "REQ-BMS-002",
            "title": "Overcurrent protection",
            "description": "System shall detect overcurrent within 10ms",
            "category": "Safety",
            "asil": "D",
            "priority": "Critical"
        },
        {
            "id": "REQ-BMS-003",
            "title": "Temperature monitoring",
            "description": "System shall monitor temperatures with 1°C accuracy",
            "category": "Safety",
            "asil": "C",
            "priority": "High"
        },
        {
            "id": "REQ-BMS-004",
            "title": "SOC estimation",
            "description": "System shall estimate SOC with 5% accuracy",
            "category": "Functional",
            "asil": "B",
            "priority": "High"
        }
    ]


@pytest.fixture
def sample_adas_config() -> Dict[str, Any]:
    """Sample ADAS configuration."""
    return {
        "system": "Adaptive Cruise Control",
        "sensors": {
            "radar": {
                "type": "77GHz",
                "range_m": 200,
                "fov_deg": 20,
                "update_rate_hz": 20
            },
            "camera": {
                "type": "Mobileye",
                "resolution": "1920x1080",
                "fov_deg": 50,
                "fps": 30
            }
        },
        "algorithms": {
            "object_detection": "YOLOv8",
            "tracking": "Kalman",
            "path_planning": "A*"
        },
        "safety": {
            "asil_level": "ASIL-B",
            "sil_level": 2,
            "redundancy": "dual-channel"
        }
    }


# ============================================================================
# Tool Adapter Fixtures
# ============================================================================

@pytest.fixture
def mock_tool_adapter():
    """Mock tool adapter for testing."""
    from tools.adapters.base_adapter import OpensourceToolAdapter

    class MockAdapter(OpensourceToolAdapter):
        def __init__(self, name="mock-tool", available=True, license_valid=True):
            self.name = name
            self.version = "1.0.0"
            self.is_available = available
            self.license_valid = license_valid
            self.execution_log = []

        def _detect(self) -> bool:
            return self.is_available

        def _check_license(self) -> bool:
            return self.license_valid

        def execute(self, command: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
            self.execution_log.append({"command": command, "parameters": parameters})
            return {
                "success": True,
                "output_dir": "/tmp/output",
                "stdout": "Command executed successfully",
                "stderr": "",
                "result": "mock_result"
            }

    return MockAdapter()


@pytest.fixture
def mock_gcc_adapter():
    """Mock GCC compiler adapter."""
    adapter = Mock()
    adapter.name = "gcc-arm-none-eabi"
    adapter.version = "10.3.1"
    adapter.is_available = True
    adapter.is_opensource = True
    adapter.execute = Mock(return_value={
        "success": True,
        "output": "a.out",
        "warnings": [],
        "errors": []
    })
    return adapter


@pytest.fixture
def mock_canoe_adapter():
    """Mock CANoe adapter (commercial tool)."""
    adapter = Mock()
    adapter.name = "vector-canoe"
    adapter.version = "16.0"
    adapter.is_available = True
    adapter.is_opensource = False
    adapter.license_valid = True
    adapter.execute = Mock(return_value={
        "success": True,
        "test_results": {"passed": 42, "failed": 0},
        "report": "/tmp/canoe_report.html"
    })
    return adapter


# ============================================================================
# LLM Council Fixtures
# ============================================================================

@pytest.fixture
def mock_claude_adapter():
    """Mock Claude adapter for testing LLM council."""
    adapter = AsyncMock()
    adapter.config = Mock()
    adapter.config.name = "claude-opus-4-6"
    adapter.config.provider = "anthropic"

    async def mock_completion(messages, system_prompt):
        response = """# Technical Analysis

I agree with the proposed approach. The architecture is sound from a safety perspective.

## Key Points
- Implements proper error handling
- Follows ISO 26262 guidelines
- Uses defensive programming techniques

## Recommendation
Proceed with implementation as proposed."""
        return response, 150.0

    adapter.get_completion = mock_completion
    return adapter


@pytest.fixture
def mock_gpt_adapter():
    """Mock GPT adapter for testing LLM council."""
    adapter = AsyncMock()
    adapter.config = Mock()
    adapter.config.name = "gpt-5.4"
    adapter.config.provider = "azure-openai"

    async def mock_completion(messages, system_prompt):
        response = """# Performance Analysis

I concur with the architectural design. Performance characteristics are excellent.

## Key Points
- Efficient memory usage
- Low latency implementation
- Scalable design

## Recommendation
Implementation approved from performance perspective."""
        return response, 120.0

    adapter.get_completion = mock_completion
    return adapter


@pytest.fixture
def mock_llm_council(mock_claude_adapter, mock_gpt_adapter):
    """Mock LLM Council for testing."""
    from tools.llm_council import LLMCouncil

    council = LLMCouncil()
    council.claude_adapter = mock_claude_adapter
    council.gpt_adapter = mock_gpt_adapter

    return council


# ============================================================================
# Skill and Agent Fixtures
# ============================================================================

@pytest.fixture
def sample_skill_definition() -> Dict[str, Any]:
    """Sample skill definition."""
    return {
        "name": "can-dbc-parser",
        "version": "1.0.0",
        "category": "network",
        "description": "Parse and analyze CAN DBC files",
        "capabilities": [
            "parse_dbc",
            "validate_signals",
            "generate_code"
        ],
        "tools_required": ["cantools"],
        "automotive_domains": ["CAN", "Vehicle Networks"],
        "asil_compatible": ["A", "B", "C", "D"]
    }


@pytest.fixture
def sample_agent_definition() -> Dict[str, Any]:
    """Sample agent definition."""
    return {
        "name": "ecu-code-generator",
        "version": "1.0.0",
        "type": "code_generation",
        "description": "Generate production-ready ECU code",
        "skills_required": [
            "autosar-code-gen",
            "misra-compliance",
            "unit-test-gen"
        ],
        "llm_model": "claude-sonnet-4-5",
        "autonomy_level": "supervised",
        "safety_critical": True
    }


@pytest.fixture
def sample_workflow_definition() -> Dict[str, Any]:
    """Sample workflow definition."""
    return {
        "name": "bms-development-workflow",
        "version": "1.0.0",
        "description": "Complete BMS development from requirements to HIL",
        "stages": [
            {
                "name": "requirements_analysis",
                "agent": "requirements-engineer",
                "inputs": ["requirements.yaml"],
                "outputs": ["analyzed_requirements.json"]
            },
            {
                "name": "architecture_design",
                "agent": "system-architect",
                "inputs": ["analyzed_requirements.json"],
                "outputs": ["architecture.yaml"]
            },
            {
                "name": "code_generation",
                "agent": "ecu-code-generator",
                "inputs": ["architecture.yaml"],
                "outputs": ["src/"]
            }
        ],
        "validation_gates": [
            "misra_compliance",
            "unit_test_coverage",
            "static_analysis"
        ]
    }


# ============================================================================
# Compliance and Safety Fixtures
# ============================================================================

@pytest.fixture
def iso26262_asil_levels() -> List[str]:
    """ISO 26262 ASIL levels."""
    return ["QM", "ASIL-A", "ASIL-B", "ASIL-C", "ASIL-D"]


@pytest.fixture
def misra_c_rules() -> Dict[str, Any]:
    """MISRA C rule categories."""
    return {
        "required": [
            {"rule": "1.1", "description": "Use of undefined behavior"},
            {"rule": "2.1", "description": "Unreachable code"},
            {"rule": "8.4", "description": "Compatible external linkage"}
        ],
        "advisory": [
            {"rule": "2.3", "description": "Unused type declaration"},
            {"rule": "2.7", "description": "Unused parameters"}
        ],
        "mandatory": [
            {"rule": "21.3", "description": "Memory allocation functions"},
            {"rule": "21.6", "description": "Standard I/O functions"}
        ]
    }


@pytest.fixture
def autosar_guidelines() -> Dict[str, Any]:
    """AUTOSAR coding guidelines."""
    return {
        "naming_conventions": {
            "type_prefix": "T_",
            "struct_prefix": "S_",
            "enum_prefix": "E_",
            "function_prefix": "Module_"
        },
        "code_metrics": {
            "cyclomatic_complexity_max": 10,
            "function_length_max": 50,
            "nesting_depth_max": 4
        }
    }


# ============================================================================
# CAN and Network Fixtures
# ============================================================================

@pytest.fixture
def sample_can_messages() -> List[Dict[str, Any]]:
    """Sample CAN message definitions."""
    return [
        {
            "id": 0x100,
            "name": "BMS_Voltages",
            "dlc": 8,
            "cycle_time_ms": 10,
            "sender": "BMS",
            "signals": [
                {"name": "Cell1_Voltage", "start_bit": 0, "length": 16, "scale": 0.001},
                {"name": "Cell2_Voltage", "start_bit": 16, "length": 16, "scale": 0.001}
            ]
        },
        {
            "id": 0x200,
            "name": "VCU_Commands",
            "dlc": 8,
            "cycle_time_ms": 100,
            "sender": "VCU",
            "signals": [
                {"name": "Charge_Request", "start_bit": 0, "length": 1},
                {"name": "Target_Current", "start_bit": 8, "length": 16, "scale": 0.1}
            ]
        }
    ]


# ============================================================================
# Test Execution Fixtures
# ============================================================================

@pytest.fixture
def event_loop():
    """Create event loop for async tests."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mock_subprocess():
    """Mock subprocess for tool execution tests."""
    mock = Mock()
    mock.run = Mock(return_value=Mock(
        returncode=0,
        stdout="Success",
        stderr=""
    ))
    return mock


# ============================================================================
# Marker Definitions
# ============================================================================

def pytest_configure(config):
    """Configure custom pytest markers."""
    config.addinivalue_line(
        "markers", "unit: Unit tests"
    )
    config.addinivalue_line(
        "markers", "integration: Integration tests"
    )
    config.addinivalue_line(
        "markers", "e2e: End-to-end tests"
    )
    config.addinivalue_line(
        "markers", "slow: Tests that take significant time"
    )
    config.addinivalue_line(
        "markers", "requires_tools: Tests requiring external tools"
    )
    config.addinivalue_line(
        "markers", "safety_critical: Tests for safety-critical functionality"
    )
    config.addinivalue_line(
        "markers", "llm_required: Tests requiring LLM API access"
    )


# ============================================================================
# Parametrization Helpers
# ============================================================================

# ECU types for parametrized testing
ECU_TYPES = ["BMS", "VCU", "MCU", "DCDC", "OBC", "PTC"]

# AUTOSAR modules
AUTOSAR_MODULES = ["Os", "Rte", "Com", "CanIf", "Can", "EcuM", "Det"]

# Tool categories
TOOL_CATEGORIES = [
    "compiler",
    "debugger",
    "analyzer",
    "simulator",
    "test_framework",
    "code_generator"
]

# Workflow types
WORKFLOW_TYPES = [
    "ecu_development",
    "adas_development",
    "battery_development",
    "calibration",
    "testing"
]
