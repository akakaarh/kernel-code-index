# drivers/mmc/core/slot-gpio.c

Subsystem: drivers/mmc

## Functions (12)

### mmc_gpio_alloc
- Return type: int
- Signature: mmc_gpio_alloc(struct mmc_host * host)
- Line: 41

### mmc_gpio_cd_irqt
- Return type: static irqreturn_t
- Signature: mmc_gpio_cd_irqt(int irq,void * dev_id)
- Line: 29

### mmc_gpio_get_cd
- Return type: int
- Signature: mmc_gpio_get_cd(struct mmc_host * host)
- Line: 90

### mmc_gpio_get_ro
- Return type: int
- Signature: mmc_gpio_get_ro(struct mmc_host * host)
- Line: 75

### mmc_gpio_set_cd_irq
- Return type: void
- Signature: mmc_gpio_set_cd_irq(struct mmc_host * host,int irq)
- Line: 64

### mmc_gpio_set_cd_wake
- Return type: int
- Signature: mmc_gpio_set_cd_wake(struct mmc_host * host,bool on)
- Line: 141

### mmc_gpiod_request_cd
- Return type: int
- Signature: mmc_gpiod_request_cd(struct mmc_host * host,const char * con_id,unsigned int idx,bool override_active_level,unsigned int debounce)
- Line: 175

### mmc_gpiod_request_cd_irq
- Return type: void
- Signature: mmc_gpiod_request_cd_irq(struct mmc_host * host)
- Line: 105

### mmc_gpiod_request_ro
- Return type: int
- Signature: mmc_gpiod_request_ro(struct mmc_host * host,const char * con_id,unsigned int idx,unsigned int debounce)
- Line: 248

### mmc_gpiod_set_cd_config
- Return type: int
- Signature: mmc_gpiod_set_cd_config(struct mmc_host * host,unsigned long config)
- Line: 223

### mmc_host_can_gpio_cd
- Return type: bool
- Signature: mmc_host_can_gpio_cd(struct mmc_host * host)
- Line: 231

### mmc_host_can_gpio_ro
- Return type: bool
- Signature: mmc_host_can_gpio_ro(struct mmc_host * host)
- Line: 278

## Structs (1)

### mmc_gpio
- Line: 19
- Members:
  - ro_gpio: gpio_desc *
  - cd_gpio: gpio_desc *
  - cd_gpio_isr: irq_handler_t
  - ro_label: char *
  - cd_label: char *
  - cd_debounce_delay_ms: u32
  - cd_irq: int
