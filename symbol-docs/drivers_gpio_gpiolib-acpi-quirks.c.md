# drivers/gpio/gpiolib-acpi-quirks.c

Subsystem: drivers/gpio

## Functions (6)

### acpi_gpio_add_to_deferred_list
- Return type: bool
- Signature: acpi_gpio_add_to_deferred_list(struct list_head * list)
- Line: 47
- Called by: acpi_gpiochip_request_interrupts

### acpi_gpio_handle_deferred_request_irqs
- Return type: static int __init
- Signature: acpi_gpio_handle_deferred_request_irqs(void)
- Line: 121
- Calls: acpi_gpio_process_deferred_list

### acpi_gpio_in_ignore_list
- Return type: bool
- Signature: acpi_gpio_in_ignore_list(enum acpi_gpio_ignore_list list,const char * controller_in,unsigned int pin_in)
- Line: 73
- Called by: acpi_gpio_irq_is_wake, acpi_gpiochip_alloc_event

### acpi_gpio_need_run_edge_events_on_boot
- Return type: int
- Signature: acpi_gpio_need_run_edge_events_on_boot(void)
- Line: 68
- Called by: acpi_gpiochip_request_irq

### acpi_gpio_remove_from_deferred_list
- Return type: void
- Signature: acpi_gpio_remove_from_deferred_list(struct list_head * list)
- Line: 60
- Called by: acpi_gpiochip_free_interrupts

### acpi_gpio_setup_params
- Return type: static int __init
- Signature: acpi_gpio_setup_params(void)
- Line: 398

## Structs (1)

### acpi_gpiolib_dmi_quirk
- Line: 133
- Members:
  - no_edge_events_on_boot: bool
  - ignore_wake: char *
  - ignore_interrupt: char *

## Variables (5)

- static **acpi_gpio_deferred_req_irqs_done** : bool (line 45)
- static **gpiolib_acpi_quirks** : const struct dmi_system_id[]__initconst (line 139)
- static **ignore_interrupt** : char * (line 30)
- static **ignore_wake** : char * (line 24)
- static **run_edge_events_on_boot** : int (line 19)
