# drivers/i2c/busses/i2c-tegra-bpmp.c

Subsystem: drivers/i2c

## Functions (11)

### tegra_bpmp_i2c_deserialize
- Return type: static int
- Signature: tegra_bpmp_i2c_deserialize(struct tegra_bpmp_i2c * i2c,struct mrq_i2c_response * response,struct i2c_msg * msgs,unsigned int num)
- Line: 126

### tegra_bpmp_i2c_func
- Return type: static u32
- Signature: tegra_bpmp_i2c_func(struct i2c_adapter * adapter)
- Line: 271

### tegra_bpmp_i2c_msg_len_check
- Return type: static int
- Signature: tegra_bpmp_i2c_msg_len_check(struct i2c_msg * msgs,unsigned int num)
- Line: 152

### tegra_bpmp_i2c_msg_xfer
- Return type: static int
- Signature: tegra_bpmp_i2c_msg_xfer(struct tegra_bpmp_i2c * i2c,struct mrq_i2c_request * request,struct mrq_i2c_response * response,bool atomic)
- Line: 174

### tegra_bpmp_i2c_probe
- Return type: static int
- Signature: tegra_bpmp_i2c_probe(struct platform_device * pdev)
- Line: 283

### tegra_bpmp_i2c_remove
- Return type: static void
- Signature: tegra_bpmp_i2c_remove(struct platform_device * pdev)
- Line: 319

### tegra_bpmp_i2c_xfer
- Return type: static int
- Signature: tegra_bpmp_i2c_xfer(struct i2c_adapter * adapter,struct i2c_msg * msgs,int num)
- Line: 259

### tegra_bpmp_i2c_xfer_atomic
- Return type: static int
- Signature: tegra_bpmp_i2c_xfer_atomic(struct i2c_adapter * adapter,struct i2c_msg * msgs,int num)
- Line: 265

### tegra_bpmp_i2c_xfer_common
- Return type: static int
- Signature: tegra_bpmp_i2c_xfer_common(struct i2c_adapter * adapter,struct i2c_msg * msgs,int num,bool atomic)
- Line: 225

### tegra_bpmp_serialize_i2c_msg
- Return type: static void
- Signature: tegra_bpmp_serialize_i2c_msg(struct tegra_bpmp_i2c * i2c,struct mrq_i2c_request * request,struct i2c_msg * msgs,unsigned int num)
- Line: 82

### tegra_bpmp_xlate_flags
- Return type: static void
- Signature: tegra_bpmp_xlate_flags(u16 flags,u16 * out)
- Line: 41

## Structs (1)

### tegra_bpmp_i2c
- Line: 28
- Members:
  - adapter: i2c_adapter
  - dev: device *
  - bpmp: tegra_bpmp *
  - bus: unsigned int

## Variables (3)

- static **tegra_bpmp_i2c_algo** : const struct i2c_algorithm (line 277)
- static **tegra_bpmp_i2c_driver** : platform_driver (line 332)
- static **tegra_bpmp_i2c_of_match** : const struct of_device_id[] (line 326)

## Macros (1)

- **SERIALI2C_HDR_SIZE** (line 26)
