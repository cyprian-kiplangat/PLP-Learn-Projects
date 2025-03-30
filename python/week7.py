import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

def load_and_explore_data():
    """Task 1: Load and explore the dataset"""
    print("Task 1: Loading and Exploring the Dataset")
    print("-----------------------------------------")
    
    try:
        # Load the Iris dataset from sklearn
        iris = load_iris()
        
        # Create a pandas DataFrame
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        
        # Add the target column (species)
        df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
        
        # Display basic information about the dataset
        print("First 5 rows of the dataset:")
        print(df.head())
        print("\nDataset shape:", df.shape)
        print("\nData types:")
        print(df.dtypes)
        
        # Check for missing values
        print("\nMissing values:")
        print(df.isna().sum())
        
        # The Iris dataset is clean, but let's demonstrate how to handle missing values
        print("\nDemonstrating missing value handling (not actually needed for Iris):")
        # Create a copy with some artificially introduced NaN values
        df_copy = df.copy()
        df_copy.iloc[1:5, 2] = np.nan
        
        print("After introducing some NaN values:")
        print("Missing values count:", df_copy.isna().sum())
        
        # Fill missing values with the mean of the column
        df_clean = df_copy.fillna(df_copy.mean())
        print("After filling NaN values with mean:")
        print("Missing values count:", df_clean.isna().sum())
        
        return df
        
    except Exception as e:
        print(f"Error loading or exploring data: {e}")
        return None

def basic_data_analysis(df):
    """Task 2: Basic data analysis"""
    print("\nTask 2: Basic Data Analysis")
    print("--------------------------")
    
    try:
        # Compute basic statistics
        print("Basic statistics of numerical columns:")
        print(df.describe())
        
        # Group by species and compute mean for each feature
        print("\nMean values for each feature grouped by species:")
        species_means = df.groupby('species').mean()
        print(species_means)
        
        # Identify patterns or interesting findings
        print("\nInteresting findings:")
        print("1. Versicolor and virginica have similar sepal lengths")
        print("2. Setosa has the smallest petal length and width")
        print("3. Virginica has the largest petal length and width")
        
        return species_means
        
    except Exception as e:
        print(f"Error during data analysis: {e}")
        return None

def data_visualization(df, species_means):
    """Task 3: Data visualization"""
    print("\nTask 3: Data Visualization")
    print("-------------------------")
    
    try:
        # Set the style for the plots
        sns.set(style="whitegrid")
        
        # 1. Line chart showing trends
        plt.figure(figsize=(10, 6))
        
        # Create a line chart of the means for each feature across species
        species_means.T.plot(marker='o')
        
        plt.title('Mean Values of Features by Species')
        plt.xlabel('Features')
        plt.ylabel('Mean Value (cm)')
        plt.legend(title='Species')
        plt.tight_layout()
        plt.savefig('line_chart.png')
        print("Line chart saved as 'line_chart.png'")
        
        # 2. Bar chart
        plt.figure(figsize=(12, 6))
        
        # Create a grouped bar chart
        species_means.plot(kind='bar', width=0.8)
        
        plt.title('Comparison of Mean Features by Species')
        plt.xlabel('Species')
        plt.ylabel('Mean Value (cm)')
        plt.legend(title='Features')
        plt.tight_layout()
        plt.savefig('bar_chart.png')
        print("Bar chart saved as 'bar_chart.png'")
        
        # 3. Histogram
        plt.figure(figsize=(14, 10))
        
        for i, feature in enumerate(df.columns[:-1]):
            plt.subplot(2, 2, i+1)
            
            # Create histograms for each feature with color by species
            for species in df['species'].unique():
                sns.histplot(df[df['species'] == species][feature], 
                             label=species, kde=True, alpha=0.6)
                
            plt.title(f'Distribution of {feature}')
            plt.xlabel(feature + ' (cm)')
            plt.ylabel('Frequency')
            plt.legend()
            
        plt.tight_layout()
        plt.savefig('histograms.png')
        print("Histograms saved as 'histograms.png'")
        
        # 4. Scatter plot
        plt.figure(figsize=(10, 8))
        
        # Create a scatter plot of sepal length vs petal length
        sns.scatterplot(
            x='sepal length (cm)', 
            y='petal length (cm)',
            hue='species',
            style='species',
            s=100,
            data=df
        )
        
        plt.title('Sepal Length vs Petal Length')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Petal Length (cm)')
        plt.legend(title='Species')
        plt.tight_layout()
        plt.savefig('scatter_plot.png')
        print("Scatter plot saved as 'scatter_plot.png'")
        
        # Bonus: Pair plot showing relationships between all features
        plt.figure(figsize=(12, 10))
        
        pair_plot = sns.pairplot(df, hue='species', height=2.5)
        pair_plot.fig.suptitle('Pair Plot of Iris Dataset Features', y=1.02)
        
        plt.tight_layout()
        plt.savefig('pair_plot.png')
        print("Pair plot saved as 'pair_plot.png'")
        
        print("\nAll visualizations complete!")
        
    except Exception as e:
        print(f"Error during data visualization: {e}")

def main():
    """Main function to run all tasks"""
    print("Iris Dataset Analysis and Visualization")
    print("======================================")
    
    # Task 1: Load and explore data
    df = load_and_explore_data()
    
    if df is not None:
        # Task 2: Basic data analysis
        species_means = basic_data_analysis(df)
        
        if species_means is not None:
            # Task 3: Data visualization
            data_visualization(df, species_means)
    
    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()