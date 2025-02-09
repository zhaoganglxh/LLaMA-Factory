import pynvml
pynvml.nvmlInit()
device_count = pynvml.nvmlDeviceGetCount()
for i in range(device_count):
    handle = pynvml.nvmlDeviceGetHandleByIndex(i)
    topo_info = pynvml.nvmlDeviceGetTopologyCommonAncestor(handle, i + 1 if i < device_count - 1 else 0)
    if topo_info.relationship == pynvml.NVML_TOPOLOGY_LINK_TYPE_NVLINK:
        print(f"NVLink is active between GPU {i} and GPU {i + 1 if i < device_count - 1 else 0}")
    else:
        print(f"NVLink is not active between GPU {i} and GPU {i + 1 if i < device_count - 1 else 0}")
pynvml.nvmlShutdown()