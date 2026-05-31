# drivers/gpio/gpio-mlxbf.c

Subsystem: drivers/gpio

## Functions (3)

### mlxbf_gpio_probe
- Return type: static int
- Signature: mlxbf_gpio_probe(struct platform_device * pdev)
- Line: 51
- Calls: gpio_generic_chip_init

### mlxbf_gpio_resume
- Return type: static int
- Signature: mlxbf_gpio_resume(struct platform_device * pdev)
- Line: 115

### mlxbf_gpio_suspend
- Return type: static int
- Signature: mlxbf_gpio_suspend(struct platform_device * pdev,pm_message_t state)
- Line: 96

## Structs (2)

### mlxbf_gpio_context_save_regs
- Line: 31
- Members:
  - scratchpad: u64
  - pad_control: u64[]
  - pin_dir_i: u64
  - pin_dir_o: u64
  - chip: gpio_generic_chip
  - base: void __iomem *
  - csave_regs: mlxbf_gpio_context_save_regs

### mlxbf_gpio_state
- Line: 40
- Members:
  - scratchpad: u64
  - pad_control: u64[]
  - pin_dir_i: u64
  - pin_dir_o: u64
  - chip: gpio_generic_chip
  - base: void __iomem *
  - csave_regs: mlxbf_gpio_context_save_regs

## Variables (2)

- static **mlxbf_gpio_acpi_match** : const struct acpi_device_id __maybe_unused[] (line 135)
- static **mlxbf_gpio_driver** : platform_driver (line 141)

## Macros (9)

- **MLXBF_GPIO_NR** (line 17)
- **MLXBF_GPIO_PAD_CONTROL_1_FIRST_WORD** (line 21)
- **MLXBF_GPIO_PAD_CONTROL_2_FIRST_WORD** (line 22)
- **MLXBF_GPIO_PAD_CONTROL_3_FIRST_WORD** (line 23)
- **MLXBF_GPIO_PAD_CONTROL_FIRST_WORD** (line 20)
- **MLXBF_GPIO_PIN_DIR_I** (line 25)
- **MLXBF_GPIO_PIN_DIR_O** (line 26)
- **MLXBF_GPIO_PIN_STATE** (line 27)
- **MLXBF_GPIO_SCRATCHPAD** (line 28)
