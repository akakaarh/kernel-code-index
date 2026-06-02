# drivers/spi/spi-tle62x0.c

Subsystem: drivers/spi

## Functions (9)

### decode_fault
- Return type: static unsigned char *
- Signature: decode_fault(unsigned int fault_code)
- Line: 78

### tle62x0_gpio_show
- Return type: static ssize_t
- Signature: tle62x0_gpio_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 133

### tle62x0_gpio_store
- Return type: static ssize_t
- Signature: tle62x0_gpio_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t len)
- Line: 147

### tle62x0_probe
- Return type: static int
- Signature: tle62x0_probe(struct spi_device * spi)
- Line: 239

### tle62x0_read
- Return type: static int
- Signature: tle62x0_read(struct tle62x0_state * st)
- Line: 57

### tle62x0_remove
- Return type: static void
- Signature: tle62x0_remove(struct spi_device * spi)
- Line: 291

### tle62x0_status_show
- Return type: static ssize_t
- Signature: tle62x0_status_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 96

### tle62x0_write
- Return type: static int
- Signature: tle62x0_write(struct tle62x0_state * st)
- Line: 38

### to_gpio_num
- Return type: static int
- Signature: to_gpio_num(struct device_attribute * attr)
- Line: 227

## Structs (1)

### tle62x0_state
- Line: 26
- Members:
  - us: spi_device *
  - lock: mutex
  - nr_gpio: unsigned int
  - gpio_state: unsigned int
  - tx_buff: unsigned char[4]
  - rx_buff: unsigned char[4]

## Variables (2)

- static **gpio_attrs** : device_attribute * [] (line 208)
- static **tle62x0_driver** : spi_driver (line 303)

## Macros (6)

- **CMD_READ** (line 18)
- **CMD_SET** (line 19)
- **DIAG_NORMAL** (line 21)
- **DIAG_OPEN** (line 23)
- **DIAG_OVERLOAD** (line 22)
- **DIAG_SHORTGND** (line 24)
