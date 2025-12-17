# Entry point for the application
#Basic python code practices for beginners
def main():
    print("Hello, World!")
    ai_provider = {"openai": 800, "azure": 230, "anthropic": 588, "cohere": 67, "ai21": 570}
    # comprehension example of list 
    popular_providers = [name for name, value in ai_provider.items() if value > 250]
    print("Popular AI Providers:", popular_providers)

    #comprehension example of set
    unique_providers = {name for name in ai_provider}
    print("Unique AI Providers:", unique_providers)
    dictioanary_comprehension_example()
    generate_comprehension_example()

def dictioanary_comprehension_example():
    ai_provider = {"openai": 800, "azure": 230, "anthropic": 588, "cohere": 67, "ai21": 570}
    # comprehension example of dictionary 
    #high value providers for last 30 days
    high_value_providers = {name: value  / 30 for name, value in ai_provider.items() if value > 300}
    print("High Value AI Providers:", high_value_providers)

def generate_comprehension_example():
    # Function to calculate total number of providers with value greater than 300
    ai_provider = {"openai": 800, "azure": 230, "anthropic": 588, "cohere": 67, "ai21": 570}
    total_provides = sum(value for value, value in ai_provider.items() if value > 300)
    print("Total High Value Providers:", total_provides)
    pass


if __name__ == "__main__":
    main()