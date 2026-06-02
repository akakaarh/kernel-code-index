# drivers/i2c/busses/i2c-digicolor.c

Subsystem: drivers/i2c

## Functions (19)

### dc_i2c_addr_cmd
- Return type: static u8
- Signature: dc_i2c_addr_cmd(struct i2c_msg * msg)
- Line: 76

### dc_i2c_cmd
- Return type: static void
- Signature: dc_i2c_cmd(struct dc_i2c * i2c,u8 cmd)
- Line: 71

### dc_i2c_cmd_status
- Return type: static int
- Signature: dc_i2c_cmd_status(struct dc_i2c * i2c)
- Line: 136

### dc_i2c_data
- Return type: static void
- Signature: dc_i2c_data(struct dc_i2c * i2c,u8 data)
- Line: 86

### dc_i2c_func
- Return type: static u32
- Signature: dc_i2c_func(struct i2c_adapter * adap)
- Line: 278

### dc_i2c_init_hw
- Return type: static int
- Signature: dc_i2c_init_hw(struct dc_i2c * i2c)
- Line: 257

### dc_i2c_irq
- Return type: static irqreturn_t
- Signature: dc_i2c_irq(int irq,void * dev_id)
- Line: 159

### dc_i2c_next_read
- Return type: static void
- Signature: dc_i2c_next_read(struct dc_i2c * i2c)
- Line: 102

### dc_i2c_probe
- Return type: static int
- Signature: dc_i2c_probe(struct platform_device * pdev)
- Line: 288

### dc_i2c_read_buf
- Return type: static void
- Signature: dc_i2c_read_buf(struct dc_i2c * i2c)
- Line: 123

### dc_i2c_read_byte
- Return type: static u8
- Signature: dc_i2c_read_byte(struct dc_i2c * i2c)
- Line: 118

### dc_i2c_remove
- Return type: static void
- Signature: dc_i2c_remove(struct platform_device * pdev)
- Line: 350

### dc_i2c_set_irq
- Return type: static void
- Signature: dc_i2c_set_irq(struct dc_i2c * i2c,int enable)
- Line: 129

### dc_i2c_start_msg
- Return type: static void
- Signature: dc_i2c_start_msg(struct dc_i2c * i2c,int first)
- Line: 143

### dc_i2c_stop
- Return type: static void
- Signature: dc_i2c_stop(struct dc_i2c * i2c)
- Line: 109

### dc_i2c_write_buf
- Return type: static void
- Signature: dc_i2c_write_buf(struct dc_i2c * i2c)
- Line: 97

### dc_i2c_write_byte
- Return type: static void
- Signature: dc_i2c_write_byte(struct dc_i2c * i2c,u8 byte)
- Line: 91

### dc_i2c_xfer
- Return type: static int
- Signature: dc_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 243

### dc_i2c_xfer_msg
- Return type: static int
- Signature: dc_i2c_xfer_msg(struct dc_i2c * i2c,struct i2c_msg * msg,int first,int last)
- Line: 213

## Structs (1)

### dc_i2c
- Line: 46
- Members:
  - adap: i2c_adapter
  - dev: device *
  - regs: void __iomem *
  - clk: clk *
  - frequency: unsigned int
  - msg: i2c_msg *
  - msgbuf_ptr: unsigned int
  - last: int
  - lock: spinlock_t
  - done: completion
  - state: int
  - error: int

## Enums (1)

### __anon06deffc60103
- Line: 62

## Variables (3)

- static **dc_i2c_algorithm** : const struct i2c_algorithm (line 283)
- static **dc_i2c_driver** : platform_driver (line 364)
- static **dc_i2c_match** : const struct of_device_id[] (line 358)

## Macros (20)

- **II_CLOCKTIME** (line 26)
- **II_CMD_GET_ACK** (line 32)
- **II_CMD_GET_NOACK** (line 33)
- **II_CMD_RESTART** (line 30)
- **II_CMD_SEND_ACK** (line 31)
- **II_CMD_START** (line 29)
- **II_CMD_STATUS_ABORT** (line 40)
- **II_CMD_STATUS_ACK_BAD** (line 39)
- **II_CMD_STATUS_ACK_GOOD** (line 38)
- **II_CMD_STATUS_NORMAL** (line 37)
- **II_CMD_STOP** (line 34)
- **II_COMMAND** (line 28)
- **II_COMMAND_COMPLETION_STATUS**(r) (line 36)
- **II_COMMAND_GO** (line 35)
- **II_CONTROL** (line 23)
- **II_CONTROL_LOCAL_RESET** (line 24)
- **II_DATA** (line 42)
- **II_INTENABLE** (line 44)
- **II_INTFLAG_CLEAR** (line 43)
- **TIMEOUT_MS** (line 21)
