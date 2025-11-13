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

if __name__ == "__main__":
    main()