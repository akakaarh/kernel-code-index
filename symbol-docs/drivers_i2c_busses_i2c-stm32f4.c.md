# drivers/i2c/busses/i2c-stm32f4.c

Subsystem: drivers/i2c

## Functions (23)

### stm32f4_i2c_clr_bits
- Return type: static void
- Signature: stm32f4_i2c_clr_bits(void __iomem * reg,u32 mask)
- Line: 139

### stm32f4_i2c_disable_irq
- Return type: static void
- Signature: stm32f4_i2c_disable_irq(struct stm32f4_i2c_dev * i2c_dev)
- Line: 144

### stm32f4_i2c_func
- Return type: static u32
- Signature: stm32f4_i2c_func(struct i2c_adapter * adap)
- Line: 746

### stm32f4_i2c_handle_read
- Return type: static void
- Signature: stm32f4_i2c_handle_read(struct stm32f4_i2c_dev * i2c_dev)
- Line: 394

### stm32f4_i2c_handle_rx_addr
- Return type: static void
- Signature: stm32f4_i2c_handle_rx_addr(struct stm32f4_i2c_dev * i2c_dev)
- Line: 486

### stm32f4_i2c_handle_rx_done
- Return type: static void
- Signature: stm32f4_i2c_handle_rx_done(struct stm32f4_i2c_dev * i2c_dev)
- Line: 434

### stm32f4_i2c_handle_write
- Return type: static void
- Signature: stm32f4_i2c_handle_write(struct stm32f4_i2c_dev * i2c_dev)
- Line: 369

### stm32f4_i2c_hw_config
- Return type: static int
- Signature: stm32f4_i2c_hw_config(struct stm32f4_i2c_dev * i2c_dev)
- Line: 280

### stm32f4_i2c_isr_error
- Return type: static irqreturn_t
- Signature: stm32f4_i2c_isr_error(int irq,void * data)
- Line: 628

### stm32f4_i2c_isr_event
- Return type: static irqreturn_t
- Signature: stm32f4_i2c_isr_event(int irq,void * data)
- Line: 556

### stm32f4_i2c_probe
- Return type: static int
- Signature: stm32f4_i2c_probe(struct platform_device * pdev)
- Line: 756

### stm32f4_i2c_read_msg
- Return type: static void
- Signature: stm32f4_i2c_read_msg(struct stm32f4_i2c_dev * i2c_dev)
- Line: 339

### stm32f4_i2c_remove
- Return type: static void
- Signature: stm32f4_i2c_remove(struct platform_device * pdev)
- Line: 853

### stm32f4_i2c_set_bits
- Return type: static void
- Signature: stm32f4_i2c_set_bits(void __iomem * reg,u32 mask)
- Line: 134

### stm32f4_i2c_set_periph_clk_freq
- Return type: static int
- Signature: stm32f4_i2c_set_periph_clk_freq(struct stm32f4_i2c_dev * i2c_dev)
- Line: 151

### stm32f4_i2c_set_rise_time
- Return type: static void
- Signature: stm32f4_i2c_set_rise_time(struct stm32f4_i2c_dev * i2c_dev)
- Line: 191

### stm32f4_i2c_set_speed_mode
- Return type: static void
- Signature: stm32f4_i2c_set_speed_mode(struct stm32f4_i2c_dev * i2c_dev)
- Line: 225

### stm32f4_i2c_terminate_xfer
- Return type: static void
- Signature: stm32f4_i2c_terminate_xfer(struct stm32f4_i2c_dev * i2c_dev)
- Line: 349

### stm32f4_i2c_wait_free_bus
- Return type: static int
- Signature: stm32f4_i2c_wait_free_bus(struct stm32f4_i2c_dev * i2c_dev)
- Line: 298

### stm32f4_i2c_write_byte
- Return type: static void
- Signature: stm32f4_i2c_write_byte(struct stm32f4_i2c_dev * i2c_dev,u8 byte)
- Line: 320

### stm32f4_i2c_write_msg
- Return type: static void
- Signature: stm32f4_i2c_write_msg(struct stm32f4_i2c_dev * i2c_dev)
- Line: 331

### stm32f4_i2c_xfer
- Return type: static int
- Signature: stm32f4_i2c_xfer(struct i2c_adapter * i2c_adap,struct i2c_msg msgs[],int num)
- Line: 725

### stm32f4_i2c_xfer_msg
- Return type: static int
- Signature: stm32f4_i2c_xfer_msg(struct stm32f4_i2c_dev * i2c_dev,struct i2c_msg * msg,bool is_first,bool is_last)
- Line: 678

## Structs (2)

### stm32f4_i2c_dev
- Line: 123
- Members:
  - addr: u8
  - count: u32
  - buf: u8 *
  - result: int
  - stop: bool
  - adap: i2c_adapter
  - dev: device *
  - base: void __iomem *
  - complete: completion
  - clk: clk *
  - speed: int
  - parent_rate: int
  - msg: stm32f4_i2c_msg

### stm32f4_i2c_msg
- Line: 104
- Members:
  - addr: u8
  - count: u32
  - buf: u8 *
  - result: int
  - stop: bool
  - adap: i2c_adapter
  - dev: device *
  - base: void __iomem *
  - complete: completion
  - clk: clk *
  - speed: int
  - parent_rate: int
  - msg: stm32f4_i2c_msg

## Variables (3)

- static **stm32f4_i2c_algo** : const struct i2c_algorithm (line 751)
- static **stm32f4_i2c_driver** : platform_driver (line 866)
- static **stm32f4_i2c_match** : const struct of_device_id[] (line 860)

## Macros (41)

- **HZ_TO_MHZ** (line 94)
- **STM32F4_I2C_CCR** (line 39)
- **STM32F4_I2C_CCR_CCR**(n) (line 83)
- **STM32F4_I2C_CCR_CCR_MASK** (line 82)
- **STM32F4_I2C_CCR_DUTY** (line 85)
- **STM32F4_I2C_CCR_FS** (line 84)
- **STM32F4_I2C_CR1** (line 34)
- **STM32F4_I2C_CR1_ACK** (line 45)
- **STM32F4_I2C_CR1_PE** (line 48)
- **STM32F4_I2C_CR1_POS** (line 44)
- **STM32F4_I2C_CR1_START** (line 47)
- **STM32F4_I2C_CR1_STOP** (line 46)
- **STM32F4_I2C_CR2** (line 35)
- **STM32F4_I2C_CR2_FREQ**(n) (line 52)
- **STM32F4_I2C_CR2_FREQ_MASK** (line 51)
- **STM32F4_I2C_CR2_IRQ_MASK** (line 56)
- **STM32F4_I2C_CR2_ITBUFEN** (line 53)
- **STM32F4_I2C_CR2_ITERREN** (line 55)
- **STM32F4_I2C_CR2_ITEVTEN** (line 54)
- **STM32F4_I2C_DR** (line 36)
- **STM32F4_I2C_FLTR** (line 41)
- **STM32F4_I2C_MAX_FREQ** (line 93)
- **STM32F4_I2C_MIN_FAST_FREQ** (line 92)
- **STM32F4_I2C_MIN_STANDARD_FREQ** (line 91)
- **STM32F4_I2C_SR1** (line 37)
- **STM32F4_I2C_SR1_ADDR** (line 67)
- **STM32F4_I2C_SR1_AF** (line 61)
- **STM32F4_I2C_SR1_ARLO** (line 62)
- **STM32F4_I2C_SR1_BERR** (line 63)
- **STM32F4_I2C_SR1_BTF** (line 66)
- **STM32F4_I2C_SR1_ITBUFEN_MASK** (line 72)
- **STM32F4_I2C_SR1_ITERREN_MASK** (line 74)
- **STM32F4_I2C_SR1_ITEVTEN_MASK** (line 69)
- **STM32F4_I2C_SR1_RXNE** (line 65)
- **STM32F4_I2C_SR1_SB** (line 68)
- **STM32F4_I2C_SR1_TXE** (line 64)
- **STM32F4_I2C_SR2** (line 38)
- **STM32F4_I2C_SR2_BUSY** (line 79)
- **STM32F4_I2C_TRISE** (line 40)
- **STM32F4_I2C_TRISE_VALUE**(n) (line 89)
- **STM32F4_I2C_TRISE_VALUE_MASK** (line 88)
