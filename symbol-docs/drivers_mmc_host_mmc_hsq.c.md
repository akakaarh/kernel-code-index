# drivers/mmc/host/mmc_hsq.c

Subsystem: drivers/mmc

## Functions (17)

### mmc_hsq_disable
- Return type: static void
- Signature: mmc_hsq_disable(struct mmc_host * mmc)
- Line: 288

### mmc_hsq_enable
- Return type: static int
- Signature: mmc_hsq_enable(struct mmc_host * mmc,struct mmc_card * card)
- Line: 318

### mmc_hsq_finalize_request
- Return type: bool
- Signature: mmc_hsq_finalize_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 153

### mmc_hsq_init
- Return type: int
- Signature: mmc_hsq_init(struct mmc_hsq * hsq,struct mmc_host * mmc)
- Line: 346

### mmc_hsq_modify_threshold
- Return type: static void
- Signature: mmc_hsq_modify_threshold(struct mmc_hsq * hsq)
- Line: 24

### mmc_hsq_post_req
- Return type: static void
- Signature: mmc_hsq_post_req(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 254

### mmc_hsq_post_request
- Return type: static void
- Signature: mmc_hsq_post_request(struct mmc_hsq * hsq)
- Line: 111

### mmc_hsq_pump_requests
- Return type: static void
- Signature: mmc_hsq_pump_requests(struct mmc_hsq * hsq)
- Line: 43

### mmc_hsq_queue_is_idle
- Return type: static bool
- Signature: mmc_hsq_queue_is_idle(struct mmc_hsq * hsq,int * ret)
- Line: 260

### mmc_hsq_recovery_finish
- Return type: static void
- Signature: mmc_hsq_recovery_finish(struct mmc_host * mmc)
- Line: 192

### mmc_hsq_recovery_start
- Return type: static void
- Signature: mmc_hsq_recovery_start(struct mmc_host * mmc)
- Line: 180

### mmc_hsq_request
- Return type: static int
- Signature: mmc_hsq_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 212

### mmc_hsq_resume
- Return type: int
- Signature: mmc_hsq_resume(struct mmc_host * mmc)
- Line: 380

### mmc_hsq_retry_handler
- Return type: static void
- Signature: mmc_hsq_retry_handler(struct work_struct * work)
- Line: 16

### mmc_hsq_suspend
- Return type: void
- Signature: mmc_hsq_suspend(struct mmc_host * mmc)
- Line: 374

### mmc_hsq_update_next_tag
- Return type: static void
- Signature: mmc_hsq_update_next_tag(struct mmc_hsq * hsq,int remains)
- Line: 92

### mmc_hsq_wait_for_idle
- Return type: static int
- Signature: mmc_hsq_wait_for_idle(struct mmc_host * mmc)
- Line: 277

## Variables (1)

- static **mmc_hsq_ops** : const struct mmc_cqe_ops (line 336)
