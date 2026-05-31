# drivers/gpio/gpio-winbond.c

Subsystem: drivers/gpio

## Functions (20)

### winbond_gpio_check_chip
- Return type: static int
- Signature: winbond_gpio_check_chip(unsigned long base)
- Line: 591
- Calls: winbond_sio_enter, winbond_sio_leave, winbond_sio_reg_read
- Called by: winbond_gpio_imatch

### winbond_gpio_configure
- Return type: static int
- Signature: winbond_gpio_configure(unsigned long base)
- Line: 575
- Calls: winbond_gpio_configure_port
- Called by: winbond_gpio_iprobe

### winbond_gpio_configure_port
- Return type: static bool
- Signature: winbond_gpio_configure_port(unsigned long base,unsigned int idx)
- Line: 526
- Calls: winbond_gpio_configure_port0_pins, winbond_gpio_configure_port1_check_i2c, winbond_sio_reg_bclear, winbond_sio_reg_bset, winbond_sio_reg_btest, winbond_sio_select_logical
- Called by: winbond_gpio_configure

### winbond_gpio_configure_port0_pins
- Return type: static void
- Signature: winbond_gpio_configure_port0_pins(unsigned long base)
- Line: 501
- Calls: winbond_sio_reg_read, winbond_sio_reg_write
- Called by: winbond_gpio_configure_port

### winbond_gpio_configure_port1_check_i2c
- Return type: static void
- Signature: winbond_gpio_configure_port1_check_i2c(unsigned long base)
- Line: 518
- Calls: winbond_sio_reg_btest
- Called by: winbond_gpio_configure_port

### winbond_gpio_direction_in
- Return type: static int
- Signature: winbond_gpio_direction_in(struct gpio_chip * gc,unsigned int offset)
- Line: 407
- Calls: gpiochip_get_data, winbond_gpio_get_info, winbond_sio_enter, winbond_sio_leave, winbond_sio_reg_bset, winbond_sio_select_logical

### winbond_gpio_direction_out
- Return type: static int
- Signature: winbond_gpio_direction_out(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 429
- Calls: gpiochip_get_data, winbond_gpio_get_info, winbond_sio_enter, winbond_sio_leave, winbond_sio_reg_bclear, winbond_sio_reg_bset, winbond_sio_reg_btest, winbond_sio_select_logical

### winbond_gpio_get
- Return type: static int
- Signature: winbond_gpio_get(struct gpio_chip * gc,unsigned int offset)
- Line: 383
- Calls: gpiochip_get_data, winbond_gpio_get_info, winbond_sio_enter, winbond_sio_leave, winbond_sio_reg_btest, winbond_sio_select_logical

### winbond_gpio_get_info
- Return type: static bool
- Signature: winbond_gpio_get_info(unsigned int * gpio_num,const struct winbond_gpio_info ** info)
- Line: 351
- Called by: winbond_gpio_direction_in, winbond_gpio_direction_out, winbond_gpio_get, winbond_gpio_set

### winbond_gpio_imatch
- Return type: static int
- Signature: winbond_gpio_imatch(struct device * dev,unsigned int id)
- Line: 616
- Calls: winbond_gpio_check_chip

### winbond_gpio_iprobe
- Return type: static int
- Signature: winbond_gpio_iprobe(struct device * dev,unsigned int id)
- Line: 652
- Calls: winbond_gpio_configure, winbond_sio_enter, winbond_sio_leave

### winbond_gpio_set
- Return type: static int
- Signature: winbond_gpio_set(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 461
- Calls: gpiochip_get_data, winbond_gpio_get_info, winbond_sio_enter, winbond_sio_leave, winbond_sio_reg_bclear, winbond_sio_reg_bset, winbond_sio_reg_btest, winbond_sio_select_logical

### winbond_sio_enter
- Return type: static int
- Signature: winbond_sio_enter(unsigned long base)
- Line: 142
- Called by: winbond_gpio_check_chip, winbond_gpio_direction_in, winbond_gpio_direction_out, winbond_gpio_get, winbond_gpio_iprobe, winbond_gpio_set

### winbond_sio_leave
- Return type: static void
- Signature: winbond_sio_leave(unsigned long base)
- Line: 163
- Called by: winbond_gpio_check_chip, winbond_gpio_direction_in, winbond_gpio_direction_out, winbond_gpio_get, winbond_gpio_iprobe, winbond_gpio_set

### winbond_sio_reg_bclear
- Return type: static void
- Signature: winbond_sio_reg_bclear(unsigned long base,u8 reg,u8 bit)
- Line: 191
- Calls: winbond_sio_reg_read, winbond_sio_reg_write
- Called by: winbond_gpio_configure_port, winbond_gpio_direction_out, winbond_gpio_set

### winbond_sio_reg_bset
- Return type: static void
- Signature: winbond_sio_reg_bset(unsigned long base,u8 reg,u8 bit)
- Line: 182
- Calls: winbond_sio_reg_read, winbond_sio_reg_write
- Called by: winbond_gpio_configure_port, winbond_gpio_direction_in, winbond_gpio_direction_out, winbond_gpio_set

### winbond_sio_reg_btest
- Return type: static bool
- Signature: winbond_sio_reg_btest(unsigned long base,u8 reg,u8 bit)
- Line: 200
- Calls: winbond_sio_reg_read
- Called by: winbond_gpio_configure_port, winbond_gpio_configure_port1_check_i2c, winbond_gpio_direction_out, winbond_gpio_get, winbond_gpio_set

### winbond_sio_reg_read
- Return type: static u8
- Signature: winbond_sio_reg_read(unsigned long base,u8 reg)
- Line: 176
- Called by: winbond_gpio_check_chip, winbond_gpio_configure_port0_pins, winbond_sio_reg_bclear, winbond_sio_reg_bset, winbond_sio_reg_btest

### winbond_sio_reg_write
- Return type: static void
- Signature: winbond_sio_reg_write(unsigned long base,u8 reg,u8 data)
- Line: 170
- Called by: winbond_gpio_configure_port0_pins, winbond_sio_reg_bclear, winbond_sio_reg_bset

### winbond_sio_select_logical
- Return type: static void
- Signature: winbond_sio_select_logical(unsigned long base,u8 dev)
- Line: 157
- Called by: winbond_gpio_configure_port, winbond_gpio_direction_in, winbond_gpio_direction_out, winbond_gpio_get, winbond_gpio_set

## Structs (3)

### winbond_gpio_info
- Line: 239
- Members:
  - base: unsigned long
  - gpios: unsigned long
  - ppgpios: unsigned long
  - odgpios: unsigned long
  - pledgpio: bool
  - beepgpio: bool
  - i2cgpio: bool
  - name: const char *
  - dev: u8
  - testreg: u8
  - testbit: u8
  - warnonly: bool
  - dev: u8
  - enablereg: u8
  - enablebit: u8
  - outputreg: u8
  - outputppbit: u8
  - ioreg: u8
  - invreg: u8
  - datareg: u8
  - conflict: winbond_gpio_port_conflict

### winbond_gpio_params
- Line: 130
- Members:
  - base: unsigned long
  - gpios: unsigned long
  - ppgpios: unsigned long
  - odgpios: unsigned long
  - pledgpio: bool
  - beepgpio: bool
  - i2cgpio: bool
  - name: const char *
  - dev: u8
  - testreg: u8
  - testbit: u8
  - warnonly: bool
  - dev: u8
  - enablereg: u8
  - enablebit: u8
  - outputreg: u8
  - outputppbit: u8
  - ioreg: u8
  - invreg: u8
  - datareg: u8
  - conflict: winbond_gpio_port_conflict

### winbond_gpio_port_conflict
- Line: 217
- Members:
  - base: unsigned long
  - gpios: unsigned long
  - ppgpios: unsigned long
  - odgpios: unsigned long
  - pledgpio: bool
  - beepgpio: bool
  - i2cgpio: bool
  - name: const char *
  - dev: u8
  - testreg: u8
  - testbit: u8
  - warnonly: bool
  - dev: u8
  - enablereg: u8
  - enablebit: u8
  - outputreg: u8
  - outputppbit: u8
  - ioreg: u8
  - invreg: u8
  - datareg: u8
  - conflict: winbond_gpio_port_conflict

## Variables (4)

- static **params** : winbond_gpio_params (line 140)
- static **winbond_gpio_chip** : gpio_chip (line 490)
- static **winbond_gpio_idriver** : isa_driver (line 689)
- static **winbond_gpio_infos** : const struct winbond_gpio_info[6] (line 251)

## Macros (79)

- **WB_GPIO_DRIVER_NAME** (line 16)
- **WB_SIO_BASE** (line 18)
- **WB_SIO_BASE_HIGH** (line 19)
- **WB_SIO_CHIP_ID_W83627UHG** (line 31)
- **WB_SIO_CHIP_ID_W83627UHG_MASK** (line 32)
- **WB_SIO_DEV_GPIO12** (line 105)
- **WB_SIO_DEV_GPIO34** (line 81)
- **WB_SIO_DEV_NONE** (line 66)
- **WB_SIO_DEV_UARTB** (line 71)
- **WB_SIO_DEV_UARTC** (line 76)
- **WB_SIO_DEV_UARTD** (line 117)
- **WB_SIO_DEV_UARTE** (line 122)
- **WB_SIO_DEV_WDGPIO56** (line 93)
- **WB_SIO_EXT_ENTER_KEY** (line 21)
- **WB_SIO_EXT_EXIT_KEY** (line 22)
- **WB_SIO_GPIO12_ENABLE_1** (line 107)
- **WB_SIO_GPIO12_ENABLE_2** (line 108)
- **WB_SIO_GPIO12_REG_DATA1** (line 110)
- **WB_SIO_GPIO12_REG_DATA2** (line 113)
- **WB_SIO_GPIO12_REG_ENABLE** (line 106)
- **WB_SIO_GPIO12_REG_INV1** (line 111)
- **WB_SIO_GPIO12_REG_INV2** (line 114)
- **WB_SIO_GPIO12_REG_IO1** (line 109)
- **WB_SIO_GPIO12_REG_IO2** (line 112)
- **WB_SIO_GPIO34_ENABLE_3** (line 83)
- **WB_SIO_GPIO34_ENABLE_4** (line 84)
- **WB_SIO_GPIO34_REG_DATA3** (line 86)
- **WB_SIO_GPIO34_REG_DATA4** (line 89)
- **WB_SIO_GPIO34_REG_ENABLE** (line 82)
- **WB_SIO_GPIO34_REG_INV3** (line 87)
- **WB_SIO_GPIO34_REG_INV4** (line 90)
- **WB_SIO_GPIO34_REG_IO3** (line 85)
- **WB_SIO_GPIO34_REG_IO4** (line 88)
- **WB_SIO_REG_CHIP_LSB** (line 29)
- **WB_SIO_REG_CHIP_MSB** (line 28)
- **WB_SIO_REG_DPD** (line 34)
- **WB_SIO_REG_DPD_UARTA** (line 35)
- **WB_SIO_REG_DPD_UARTB** (line 36)
- **WB_SIO_REG_G1MF_FS_GPIO1** (line 62)
- **WB_SIO_REG_G1MF_FS_IR** (line 61)
- **WB_SIO_REG_G1MF_FS_IR_OFF** (line 60)
- **WB_SIO_REG_G1MF_FS_MASK** (line 59)
- **WB_SIO_REG_G1MF_FS_UARTB** (line 63)
- **WB_SIO_REG_G1MF_G1PP** (line 57)
- **WB_SIO_REG_G1MF_G2PP** (line 58)
- **WB_SIO_REG_GLOBAL_OPT** (line 44)
- **WB_SIO_REG_GO_ENFDC** (line 45)
- **WB_SIO_REG_GPIO1_MF** (line 56)
- **WB_SIO_REG_I2CPS_I2CFS** (line 54)
- **WB_SIO_REG_I2C_PS** (line 53)
- **WB_SIO_REG_IDPD** (line 38)
- **WB_SIO_REG_IDPD_UARTC** (line 39)
- **WB_SIO_REG_IDPD_UARTD** (line 40)
- **WB_SIO_REG_IDPD_UARTE** (line 41)
- **WB_SIO_REG_IDPD_UARTF** (line 42)
- **WB_SIO_REG_LOGICAL** (line 26)
- **WB_SIO_REG_OG3456_G3PP** (line 48)
- **WB_SIO_REG_OG3456_G4PP** (line 49)
- **WB_SIO_REG_OG3456_G5PP** (line 50)
- **WB_SIO_REG_OG3456_G6PP** (line 51)
- **WB_SIO_REG_OVTGPIO3456** (line 47)
- **WB_SIO_UARTB_ENABLE_ON** (line 73)
- **WB_SIO_UARTB_REG_ENABLE** (line 72)
- **WB_SIO_UARTC_ENABLE_ON** (line 78)
- **WB_SIO_UARTC_REG_ENABLE** (line 77)
- **WB_SIO_UARTD_ENABLE_ON** (line 119)
- **WB_SIO_UARTD_REG_ENABLE** (line 118)
- **WB_SIO_UARTE_ENABLE_ON** (line 124)
- **WB_SIO_UARTE_REG_ENABLE** (line 123)
- **WB_SIO_WDGPIO56_ENABLE_5** (line 95)
- **WB_SIO_WDGPIO56_ENABLE_6** (line 96)
- **WB_SIO_WDGPIO56_REG_DATA5** (line 98)
- **WB_SIO_WDGPIO56_REG_DATA6** (line 101)
- **WB_SIO_WDGPIO56_REG_ENABLE** (line 94)
- **WB_SIO_WDGPIO56_REG_INV5** (line 99)
- **WB_SIO_WDGPIO56_REG_INV6** (line 102)
- **WB_SIO_WDGPIO56_REG_IO5** (line 97)
- **WB_SIO_WDGPIO56_REG_IO6** (line 100)
- **pr_fmt**(fmt) (line 9)
