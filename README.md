# oneshot

Github Action for zero or one shot prompting with chat gpt model from OpenAI.

## Usage

```yaml
steps:
- uses: actions/checkout@v3
- uses: belizwp/oneshot@main
  with:
    openai_api_key: ${{ secrets.OPENAI_API_KEY }}
    prompt: "How are you?"
- shell: bash
  run: |
    echo "The answer is ${{ steps.oneshot.outputs.output }}"
```
