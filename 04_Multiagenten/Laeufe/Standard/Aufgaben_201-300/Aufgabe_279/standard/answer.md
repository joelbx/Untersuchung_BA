Decoupled payment token creation from verification. The five requested components now use `getDefaultVerifyPayment` and `getCreatePaymentToken`; the helper handles chargeable, pending, and failed token statuses explicitly. Polling stops on completion or cancellation.

The component type check and relevant payment, subscription, and signup tests pass.