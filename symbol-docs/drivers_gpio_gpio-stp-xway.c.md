# drivers/gpio/gpio-stp-xway.c

Subsystem: drivers/gpio

## Functions (7)

### xway_stp_dir_out
- Return type: static int
- Signature: xway_stp_dir_out(struct gpio_chip * gc,unsigned gpio,int val)
- Line: 139
- Calls: xway_stp_set

### xway_stp_get
- Return type: static int
- Signature: xway_stp_get(struct gpio_chip * gc,unsigned int gpio)
- Line: 101
- Calls: gpiochip_get_data

### xway_stp_hw_init
- Return type: static void
- Signature: xway_stp_hw_init(struct xway_stp * chip)
- Line: 167
- Called by: xway_stp_probe

### xway_stp_init
- Return type: static int __init
- Signature: xway_stp_init(void)
- Line: 330

### xway_stp_probe
- Return type: static int
- Signature: xway_stp_probe(struct platform_device * pdev)
- Line: 233
- Calls: xway_stp_hw_init

### xway_stp_request
- Return type: static int
- Signature: xway_stp_request(struct gpio_chip * gc,unsigned gpio)
- Line: 151
- Calls: gpiochip_get_data

### xway_stp_set
- Return type: static int
- Signature: xway_stp_set(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 116
- Calls: gpiochip_get_data
- Called by: xway_stp_dir_out

## Structs (1)

### xway_stp
- Line: 80
- Members:
  - gc: gpio_chip
  - virt: void __iomem *
  - edge: u32
  - shadow: u32
  - groups: u8
  - dsl: u8
  - phy1: u8
  - phy2: u8
  - phy3: u8
  - phy4: u8
  - reserved: u8

## Variables (2)

- static **xway_stp_driver** : platform_driver (line 322)
- static **xway_stp_match** : const struct of_device_id[] (line 316)

## Macros (31)

- **XWAY_STP_10HZ** (line 44)
- **XWAY_STP_2HZ** (line 41)
- **XWAY_STP_4HZ** (line 42)
- **XWAY_STP_8HZ** (line 43)
- **XWAY_STP_ADSL_MASK** (line 56)
- **XWAY_STP_ADSL_SHIFT** (line 55)
- **XWAY_STP_AR** (line 35)
- **XWAY_STP_CON0** (line 27)
- **XWAY_STP_CON1** (line 29)
- **XWAY_STP_CON_SWU** (line 38)
- **XWAY_STP_CPU0** (line 31)
- **XWAY_STP_CPU1** (line 33)
- **XWAY_STP_EDGE_MASK** (line 73)
- **XWAY_STP_FALLING** (line 72)
- **XWAY_STP_FPIS_MASK** (line 48)
- **XWAY_STP_FPIS_VALUE** (line 47)
- **XWAY_STP_GROUP0** (line 66)
- **XWAY_STP_GROUP1** (line 67)
- **XWAY_STP_GROUP2** (line 68)
- **XWAY_STP_GROUP_MASK** (line 69)
- **XWAY_STP_PHY1_SHIFT** (line 60)
- **XWAY_STP_PHY2_SHIFT** (line 61)
- **XWAY_STP_PHY3_SHIFT** (line 62)
- **XWAY_STP_PHY4_SHIFT** (line 63)
- **XWAY_STP_PHY_MASK** (line 59)
- **XWAY_STP_SPEED_MASK** (line 45)
- **XWAY_STP_UPD_FPI** (line 51)
- **XWAY_STP_UPD_MASK** (line 52)
- **xway_stp_r32**(m,reg) (line 75)
- **xway_stp_w32**(m,val,reg) (line 76)
- **xway_stp_w32_mask**(m,clear,set,reg) (line 77)
