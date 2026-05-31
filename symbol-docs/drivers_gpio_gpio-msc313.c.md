# drivers/gpio/gpio-msc313.c

Subsystem: drivers/gpio

## Functions (11)

### msc313_gpio_direction_input
- Return type: static int
- Signature: msc313_gpio_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 511
- Calls: gpiochip_get_data

### msc313_gpio_direction_output
- Return type: static int
- Signature: msc313_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 522
- Calls: gpiochip_get_data

### msc313_gpio_get
- Return type: static int
- Signature: msc313_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 504
- Calls: gpiochip_get_data

### msc313_gpio_irq_mask
- Return type: static void
- Signature: msc313_gpio_irq_mask(struct irq_data * d)
- Line: 537
- Calls: gpiochip_disable_irq

### msc313_gpio_irq_unmask
- Return type: static void
- Signature: msc313_gpio_irq_unmask(struct irq_data * d)
- Line: 545
- Calls: gpiochip_enable_irq

### msc313_gpio_populate_parent_fwspec
- Return type: static int
- Signature: msc313_gpio_populate_parent_fwspec(struct gpio_chip * gc,union gpio_irq_fwspec * gfwspec,unsigned int parent_hwirq,unsigned int parent_type)
- Line: 573

### msc313_gpio_probe
- Return type: static int
- Signature: msc313_gpio_probe(struct platform_device * pdev)
- Line: 612

### msc313_gpio_resume
- Return type: static int
- Signature: msc313_gpio_resume(struct device * dev)
- Line: 708

### msc313_gpio_set
- Return type: static int
- Signature: msc313_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 489
- Calls: gpiochip_get_data

### msc313_gpio_suspend
- Return type: static int
- Signature: msc313_gpio_suspend(struct device * dev)
- Line: 697

### msc313e_gpio_child_to_parent_hwirq
- Return type: static int
- Signature: msc313e_gpio_child_to_parent_hwirq(struct gpio_chip * chip,unsigned int child,unsigned int child_type,unsigned int * parent,unsigned int * parent_type)
- Line: 589
- Calls: gpiochip_get_data

## Structs (2)

### msc313_gpio
- Line: 483
- Members:
  - names: const char * const *
  - offsets: const unsigned int *
  - num: const unsigned int
  - base: void __iomem *
  - gpio_data: const struct msc313_gpio_data *
  - saved: u8 *

### msc313_gpio_data
- Line: 193
- Members:
  - names: const char * const *
  - offsets: const unsigned int *
  - num: const unsigned int
  - base: void __iomem *
  - gpio_data: const struct msc313_gpio_data *
  - saved: u8 *

## Variables (7)

- static **msc313_gpio_driver** : platform_driver (line 721)
- static **msc313_gpio_irqchip** : const struct irq_chip (line 557)
- static **msc313_gpio_of_match** : const struct of_device_id[] (line 678)
- static **msc313_names** : const char * const[] (line 207)
- static **msc313_offsets** : const unsigned int[] (line 215)
- static **ssd20xd_names** : const char * const[] (line 462)
- static **ssd20xd_offsets** : const unsigned int[] (line 471)

## Macros (191)

- **DRIVER_NAME** (line 18)
- **FUART_NAMES** (line 72)
- **FUART_OFFSETS** (line 83)
- **I2C1_NAMES** (line 165)
- **I2C1_OFFSETS** (line 172)
- **MSC313_GPIO_BITSTOSAVE** (line 28)
- **MSC313_GPIO_CHIPDATA**(_chip) (line 199)
- **MSC313_GPIO_IN** (line 20)
- **MSC313_GPIO_OEN** (line 22)
- **MSC313_GPIO_OUT** (line 21)
- **MSC313_PINNAME_FUART_CTS** (line 33)
- **MSC313_PINNAME_FUART_RTS** (line 34)
- **MSC313_PINNAME_FUART_RX** (line 31)
- **MSC313_PINNAME_FUART_TX** (line 32)
- **MSC313_PINNAME_I2C1_SCA** (line 64)
- **MSC313_PINNAME_I2C1_SCL** (line 63)
- **MSC313_PINNAME_SD_CLK** (line 55)
- **MSC313_PINNAME_SD_CMD** (line 56)
- **MSC313_PINNAME_SD_D0** (line 57)
- **MSC313_PINNAME_SD_D1** (line 58)
- **MSC313_PINNAME_SD_D2** (line 59)
- **MSC313_PINNAME_SD_D3** (line 60)
- **MSC313_PINNAME_SPI0_CK** (line 68)
- **MSC313_PINNAME_SPI0_CZ** (line 67)
- **MSC313_PINNAME_SPI0_DI** (line 69)
- **MSC313_PINNAME_SPI0_DO** (line 70)
- **MSC313_PINNAME_SR_IO10** (line 45)
- **MSC313_PINNAME_SR_IO11** (line 46)
- **MSC313_PINNAME_SR_IO12** (line 47)
- **MSC313_PINNAME_SR_IO13** (line 48)
- **MSC313_PINNAME_SR_IO14** (line 49)
- **MSC313_PINNAME_SR_IO15** (line 50)
- **MSC313_PINNAME_SR_IO16** (line 51)
- **MSC313_PINNAME_SR_IO17** (line 52)
- **MSC313_PINNAME_SR_IO2** (line 37)
- **MSC313_PINNAME_SR_IO3** (line 38)
- **MSC313_PINNAME_SR_IO4** (line 39)
- **MSC313_PINNAME_SR_IO5** (line 40)
- **MSC313_PINNAME_SR_IO6** (line 41)
- **MSC313_PINNAME_SR_IO7** (line 42)
- **MSC313_PINNAME_SR_IO8** (line 43)
- **MSC313_PINNAME_SR_IO9** (line 44)
- **OFF_FUART_CTS** (line 80)
- **OFF_FUART_RTS** (line 81)
- **OFF_FUART_RX** (line 78)
- **OFF_FUART_TX** (line 79)
- **OFF_I2C1_SCA** (line 170)
- **OFF_I2C1_SCL** (line 169)
- **OFF_SD_CLK** (line 150)
- **OFF_SD_CMD** (line 151)
- **OFF_SD_D0** (line 152)
- **OFF_SD_D1** (line 153)
- **OFF_SD_D2** (line 154)
- **OFF_SD_D3** (line 155)
- **OFF_SPI0_CK** (line 183)
- **OFF_SPI0_CZ** (line 182)
- **OFF_SPI0_DI** (line 184)
- **OFF_SPI0_DO** (line 185)
- **OFF_SR_IO10** (line 115)
- **OFF_SR_IO11** (line 116)
- **OFF_SR_IO12** (line 117)
- **OFF_SR_IO13** (line 118)
- **OFF_SR_IO14** (line 119)
- **OFF_SR_IO15** (line 120)
- **OFF_SR_IO16** (line 121)
- **OFF_SR_IO17** (line 122)
- **OFF_SR_IO2** (line 107)
- **OFF_SR_IO3** (line 108)
- **OFF_SR_IO4** (line 109)
- **OFF_SR_IO5** (line 110)
- **OFF_SR_IO6** (line 111)
- **OFF_SR_IO7** (line 112)
- **OFF_SR_IO8** (line 113)
- **OFF_SR_IO9** (line 114)
- **SD_NAMES** (line 142)
- **SD_OFFSETS** (line 157)
- **SPI0_NAMES** (line 176)
- **SPI0_OFFSETS** (line 187)
- **SR_NAMES** (line 89)
- **SR_OFFSETS** (line 124)
- **SSD20XD_GPIO_NAMES** (line 247)
- **SSD20XD_GPIO_OFFSETS** (line 281)
- **SSD20XD_GPIO_OFF_GPIO0** (line 264)
- **SSD20XD_GPIO_OFF_GPIO1** (line 265)
- **SSD20XD_GPIO_OFF_GPIO10** (line 272)
- **SSD20XD_GPIO_OFF_GPIO11** (line 273)
- **SSD20XD_GPIO_OFF_GPIO12** (line 274)
- **SSD20XD_GPIO_OFF_GPIO13** (line 275)
- **SSD20XD_GPIO_OFF_GPIO14** (line 276)
- **SSD20XD_GPIO_OFF_GPIO2** (line 266)
- **SSD20XD_GPIO_OFF_GPIO3** (line 267)
- **SSD20XD_GPIO_OFF_GPIO4** (line 268)
- **SSD20XD_GPIO_OFF_GPIO5** (line 269)
- **SSD20XD_GPIO_OFF_GPIO6** (line 270)
- **SSD20XD_GPIO_OFF_GPIO7** (line 271)
- **SSD20XD_GPIO_OFF_GPIO85** (line 277)
- **SSD20XD_GPIO_OFF_GPIO86** (line 278)
- **SSD20XD_GPIO_OFF_GPIO90** (line 279)
- **SSD20XD_OFF_SD_CLK** (line 453)
- **SSD20XD_OFF_SD_CMD** (line 452)
- **SSD20XD_OFF_SD_D0** (line 448)
- **SSD20XD_OFF_SD_D1** (line 449)
- **SSD20XD_OFF_SD_D2** (line 450)
- **SSD20XD_OFF_SD_D3** (line 451)
- **SSD20XD_OFF_UART0_RX** (line 430)
- **SSD20XD_OFF_UART0_TX** (line 431)
- **SSD20XD_OFF_UART1_RX** (line 437)
- **SSD20XD_OFF_UART1_TX** (line 438)
- **SSD20XD_PINNAME_GPIO0** (line 230)
- **SSD20XD_PINNAME_GPIO1** (line 231)
- **SSD20XD_PINNAME_GPIO10** (line 238)
- **SSD20XD_PINNAME_GPIO11** (line 239)
- **SSD20XD_PINNAME_GPIO12** (line 240)
- **SSD20XD_PINNAME_GPIO13** (line 241)
- **SSD20XD_PINNAME_GPIO14** (line 242)
- **SSD20XD_PINNAME_GPIO2** (line 232)
- **SSD20XD_PINNAME_GPIO3** (line 233)
- **SSD20XD_PINNAME_GPIO4** (line 234)
- **SSD20XD_PINNAME_GPIO5** (line 235)
- **SSD20XD_PINNAME_GPIO6** (line 236)
- **SSD20XD_PINNAME_GPIO7** (line 237)
- **SSD20XD_PINNAME_GPIO85** (line 243)
- **SSD20XD_PINNAME_GPIO86** (line 244)
- **SSD20XD_PINNAME_GPIO90** (line 245)
- **SSD20XD_PINNAME_TTL0** (line 299)
- **SSD20XD_PINNAME_TTL1** (line 300)
- **SSD20XD_PINNAME_TTL10** (line 309)
- **SSD20XD_PINNAME_TTL11** (line 310)
- **SSD20XD_PINNAME_TTL12** (line 311)
- **SSD20XD_PINNAME_TTL13** (line 312)
- **SSD20XD_PINNAME_TTL14** (line 313)
- **SSD20XD_PINNAME_TTL15** (line 314)
- **SSD20XD_PINNAME_TTL16** (line 315)
- **SSD20XD_PINNAME_TTL17** (line 316)
- **SSD20XD_PINNAME_TTL18** (line 317)
- **SSD20XD_PINNAME_TTL19** (line 318)
- **SSD20XD_PINNAME_TTL2** (line 301)
- **SSD20XD_PINNAME_TTL20** (line 319)
- **SSD20XD_PINNAME_TTL21** (line 320)
- **SSD20XD_PINNAME_TTL22** (line 321)
- **SSD20XD_PINNAME_TTL23** (line 322)
- **SSD20XD_PINNAME_TTL24** (line 323)
- **SSD20XD_PINNAME_TTL25** (line 324)
- **SSD20XD_PINNAME_TTL26** (line 325)
- **SSD20XD_PINNAME_TTL27** (line 326)
- **SSD20XD_PINNAME_TTL3** (line 302)
- **SSD20XD_PINNAME_TTL4** (line 303)
- **SSD20XD_PINNAME_TTL5** (line 304)
- **SSD20XD_PINNAME_TTL6** (line 305)
- **SSD20XD_PINNAME_TTL7** (line 306)
- **SSD20XD_PINNAME_TTL8** (line 307)
- **SSD20XD_PINNAME_TTL9** (line 308)
- **SSD20XD_PINNAME_UART0_RX** (line 416)
- **SSD20XD_PINNAME_UART0_TX** (line 417)
- **SSD20XD_PINNAME_UART1_RX** (line 423)
- **SSD20XD_PINNAME_UART1_TX** (line 424)
- **SSD20XD_SD_OFFSETS** (line 455)
- **SSD20XD_TTL_OFFSETS** (line 386)
- **SSD20XD_TTL_OFFSET_TTL0** (line 357)
- **SSD20XD_TTL_OFFSET_TTL1** (line 358)
- **SSD20XD_TTL_OFFSET_TTL10** (line 367)
- **SSD20XD_TTL_OFFSET_TTL11** (line 368)
- **SSD20XD_TTL_OFFSET_TTL12** (line 369)
- **SSD20XD_TTL_OFFSET_TTL13** (line 370)
- **SSD20XD_TTL_OFFSET_TTL14** (line 371)
- **SSD20XD_TTL_OFFSET_TTL15** (line 372)
- **SSD20XD_TTL_OFFSET_TTL16** (line 373)
- **SSD20XD_TTL_OFFSET_TTL17** (line 374)
- **SSD20XD_TTL_OFFSET_TTL18** (line 375)
- **SSD20XD_TTL_OFFSET_TTL19** (line 376)
- **SSD20XD_TTL_OFFSET_TTL2** (line 359)
- **SSD20XD_TTL_OFFSET_TTL20** (line 377)
- **SSD20XD_TTL_OFFSET_TTL21** (line 378)
- **SSD20XD_TTL_OFFSET_TTL22** (line 379)
- **SSD20XD_TTL_OFFSET_TTL23** (line 380)
- **SSD20XD_TTL_OFFSET_TTL24** (line 381)
- **SSD20XD_TTL_OFFSET_TTL25** (line 382)
- **SSD20XD_TTL_OFFSET_TTL26** (line 383)
- **SSD20XD_TTL_OFFSET_TTL27** (line 384)
- **SSD20XD_TTL_OFFSET_TTL3** (line 360)
- **SSD20XD_TTL_OFFSET_TTL4** (line 361)
- **SSD20XD_TTL_OFFSET_TTL5** (line 362)
- **SSD20XD_TTL_OFFSET_TTL6** (line 363)
- **SSD20XD_TTL_OFFSET_TTL7** (line 364)
- **SSD20XD_TTL_OFFSET_TTL8** (line 365)
- **SSD20XD_TTL_OFFSET_TTL9** (line 366)
- **SSD20XD_TTL_PINNAMES** (line 328)
- **SSD20XD_UART0_NAMES** (line 419)
- **SSD20XD_UART0_OFFSETS** (line 433)
- **SSD20XD_UART1_NAMES** (line 426)
- **SSD20XD_UART1_OFFSETS** (line 440)
