# drivers/i2c/busses/i2c-parport.c

Subsystem: drivers/i2c

## Functions (14)

### i2c_parport_attach
- Return type: static void
- Signature: i2c_parport_attach(struct parport * port)
- Line: 264

### i2c_parport_detach
- Return type: static void
- Signature: i2c_parport_detach(struct parport * port)
- Line: 372

### i2c_parport_irq
- Return type: static void
- Signature: i2c_parport_irq(void * data)
- Line: 251

### line_get
- Return type: static int
- Signature: line_get(struct parport * data,const struct lineop * op)
- Line: 204

### line_set
- Return type: static void
- Signature: line_set(struct parport * data,int state,const struct lineop * op)
- Line: 192

### parport_getscl
- Return type: static int
- Signature: parport_getscl(void * data)
- Line: 225

### parport_getsda
- Return type: static int
- Signature: parport_getsda(void * data)
- Line: 230

### parport_setscl
- Return type: static void
- Signature: parport_setscl(void * data,int state)
- Line: 215

### parport_setsda
- Return type: static void
- Signature: parport_setsda(void * data,int state)
- Line: 220

### port_read_control
- Return type: static unsigned char
- Signature: port_read_control(struct parport * p)
- Line: 173

### port_read_data
- Return type: static unsigned char
- Signature: port_read_data(struct parport * p)
- Line: 163

### port_read_status
- Return type: static unsigned char
- Signature: port_read_status(struct parport * p)
- Line: 168

### port_write_control
- Return type: static void
- Signature: port_write_control(struct parport * p,unsigned char d)
- Line: 158

### port_write_data
- Return type: static void
- Signature: port_write_data(struct parport * p,unsigned char d)
- Line: 153

## Structs (3)

### adapter_parm
- Line: 39
- Members:
  - val: u8
  - port: u8
  - inverted: u8
  - setsda: lineop
  - setscl: lineop
  - getsda: lineop
  - getscl: lineop
  - init: lineop
  - smbus_alert: unsigned int:1
  - pdev: pardevice *
  - adapter: i2c_adapter
  - algo_data: i2c_algo_bit_data
  - alert_data: i2c_smbus_alert_setup
  - ara: i2c_client *
  - node: list_head

### i2c_par
- Line: 115
- Members:
  - val: u8
  - port: u8
  - inverted: u8
  - setsda: lineop
  - setscl: lineop
  - getsda: lineop
  - getscl: lineop
  - init: lineop
  - smbus_alert: unsigned int:1
  - pdev: pardevice *
  - adapter: i2c_adapter
  - algo_data: i2c_algo_bit_data
  - alert_data: i2c_smbus_alert_setup
  - ara: i2c_client *
  - node: list_head

### lineop
- Line: 33
- Members:
  - val: u8
  - port: u8
  - inverted: u8
  - setsda: lineop
  - setscl: lineop
  - getsda: lineop
  - getscl: lineop
  - init: lineop
  - smbus_alert: unsigned int:1
  - pdev: pardevice *
  - adapter: i2c_adapter
  - algo_data: i2c_algo_bit_data
  - alert_data: i2c_smbus_alert_setup
  - ara: i2c_client *
  - node: list_head

## Variables (7)

- static **adapter_parm** : const struct adapter_parm[] (line 48)
- static **i2c_parport_driver** : parport_driver (line 399)
- static **parport** : int[] (line 128)
- static **parport_algo_data** : const struct i2c_algo_bit_data (line 240)
- static **port_read** : unsigned char (* const[])(struct parport *) (line 184)
- static **port_write** : void (* const[])(struct parport *,unsigned char) (line 178)
- static **type** : int (line 136)

## Macros (5)

- **MAX_DEVICE** (line 127)
- **PORT_CTRL** (line 31)
- **PORT_DATA** (line 29)
- **PORT_STAT** (line 30)
- **pr_fmt**(fmt) (line 15)
