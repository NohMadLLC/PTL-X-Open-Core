###############################################################################
# PTL-X OPEN CORE SIMULATION (v1.0)
# 
# STRICT IP BOUNDARY NOTICE:
# This implementation contains ONLY the non-proprietary open-core PTL-X equation 
# as defined in Brown, B. (2025). PTL-X: Recursive Temporal Distortion Model.
#
# PROTECTED COMPONENTS EXCLUDED:
#   - Dynamic coefficient adaptation systems
#   - Cryptographic input validation protocols
#   - Bio-recursive collapse detection algorithms
#   - Hardware implementation (EEG + QRNG fusion)
#   - Clinical calibration tables and scoring interfaces
#
# Copyright (c) 2025 Breezon Brown, NohMad LLC
# Licensed for academic, educational, and non-commercial use only.
# Commercial use, clinical deployment, or derivative systems prohibited.
# Patent Protected: US 63/847,201
###############################################################################

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap

# --- SECURE PARAMETERS (Open-core only) ---
# Non-optimized placeholders (≠ clinical calibration tables)
ALPHA = 1.0    # Empirical range: [0.8, 1.2] (protected)
BETA = 0.5     # Sensitivity amplifier (protected optimization)
GAMMA = 0.1    # Stabilization constant (γ > 0)

# --- CORE EQUATION IMPLEMENTATION ---
def ptlx_open_core(M, E, R):
    """
    Computes time distortion T' using open-core PTL-X equation
    Formula: T' = α ⋅ tanh( (β ⋅ (M ⋅ E)) / (R + γ) )
    
    M: Memory density [0,1]
    E: Emotional charge [0,1]
    R: Recursive intensity [0,1]
    """
    return ALPHA * np.tanh((BETA * (M * E)) / (R + GAMMA))

# --- SYNTHETIC DATA GENERATION ---
def generate_trauma_profiles(n=1000, profiles=None):
    """
    Generates synthetic trauma profiles with controlled characteristics
    Profiles: None for random, or dict of {profile_name: {M_range, E_range, R_range}}
    """
    np.random.seed(42)  # Fixed seed for reproducibility
    
    if not profiles:
        # Default: Uniform random across all parameters
        M = np.random.uniform(0, 1, n)
        E = np.random.uniform(0, 1, n)
        R = np.random.uniform(0, 1, n)
        return M, E, R, ['Uniform']*n
    
    else:
        # Profile-based generation
        M, E, R, labels = [], [], [], []
        samples_per_profile = n // len(profiles)
        
        for profile, params in profiles.items():
            M.extend(np.random.uniform(*params['M_range'], samples_per_profile))
            E.extend(np.random.uniform(*params['E_range'], samples_per_profile))
            R.extend(np.random.uniform(*params['R_range'], samples_per_profile))
            labels.extend([profile]*samples_per_profile)
        
        return np.array(M), np.array(E), np.array(R), labels

# --- VISUALIZATION ---
def visualize_results(M, E, R, T_prime, labels=None):
    """Creates publication-quality visualizations of PTL-X open-core behavior"""
    # Custom trauma colormap (purple → red)
    trauma_cmap = LinearSegmentedColormap.from_list('trauma', ['#4b0082', '#ff0000'])
    
    plt.figure(figsize=(12, 10))
    
    # 1. Phase Space: E vs T' colored by M
    plt.subplot(2, 2, 1)
    sc = plt.scatter(E, T_prime, c=M, cmap=trauma_cmap, alpha=0.7, edgecolor='k', s=40)
    plt.title("Emotional Charge vs Time Distortion")
    plt.xlabel("Emotional Charge (E)")
    plt.ylabel("Subjective Time Distortion (T')")
    cbar = plt.colorbar(sc, shrink=0.8)
    cbar.set_label('Memory Density (M)')
    plt.grid(alpha=0.2)
    
    # 2. Recursion Impact: R vs T' colored by E
    plt.subplot(2, 2, 2)
    sc = plt.scatter(R, T_prime, c=E, cmap='viridis', alpha=0.7, edgecolor='k', s=40)
    plt.title("Recursion Intensity vs Time Distortion")
    plt.xlabel("Recursive Intensity (R)")
    plt.ylabel("Subjective Time Distortion (T')")
    cbar = plt.colorbar(sc, shrink=0.8)
    cbar.set_label('Emotional Charge (E)')
    plt.grid(alpha=0.2)
    
    # 3. 3D Relationship (M, E, T')
    ax = plt.subplot(2, 2, 3, projection='3d')
    sc = ax.scatter(M, E, T_prime, c=R, cmap='plasma', alpha=0.7, s=30)
    ax.set_title("Memory-Emotion-Time Distortion Space")
    ax.set_xlabel("Memory Density (M)")
    ax.set_ylabel("Emotional Charge (E)")
    ax.set_zlabel("Time Distortion (T')")
    ax.grid(True)
    plt.colorbar(sc, ax=ax, shrink=0.6, label='Recursion (R)')
    
    # 4. Distribution Analysis
    plt.subplot(2, 2, 4)
    if labels:
        for profile in set(labels):
            idx = [i for i, x in enumerate(labels) if x == profile]
            plt.hist(T_prime[idx], bins=30, alpha=0.6, label=profile)
    else:
        plt.hist(T_prime, bins=30, alpha=0.6, color='purple')
    plt.title("Time Distortion Distribution")
    plt.xlabel("T'")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(alpha=0.2)
    
    plt.tight_layout()
    plt.savefig('PTLX_OpenCore_Analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # ===== SIMULATION CONFIGURATION =====
    n_samples = 1000
    
    # Profile definitions (synthetic only)
    trauma_profiles = {
        'Acute Flashback': {'M_range': (0.7, 0.9), 'E_range': (0.8, 1.0), 'R_range': (0.1, 0.3)},
        'Chronic Avoidance': {'M_range': (0.4, 0.6), 'E_range': (0.5, 0.7), 'R_range': (0.6, 0.8)},
        'High-Functioning': {'M_range': (0.2, 0.4), 'E_range': (0.3, 0.5), 'R_range': (0.7, 0.9)}
    }
    
    # Generate synthetic data
    M, E, R, labels = generate_trauma_profiles(n_samples, trauma_profiles)
    
    # Compute time distortion
    T_prime = ptlx_open_core(M, E, R)
    
    # Save data (open-core format)
    df = pd.DataFrame({
        'Profile': labels,
        'MemoryDensity': M,
        'EmotionalCharge': E,
        'Recursion': R,
        'TimeDistortion': T_prime
    })
    df.to_csv('PTLX_OpenCore_Simulation.csv', index=False)
    
    # Generate comprehensive visualization
    visualize_results(M, E, R, T_prime, labels)
    
    # Security notice output
    print("\n" + "="*70)
    print("PTL-X OPEN CORE SIMULATION COMPLETED")
    print(f"- Generated {n_samples} synthetic samples")
    print("- Outputs: CSV data, visualization PNG")
    print("="*70)
    print("SECURITY NOTICE: This simulation uses ONLY the open-core equation")
    print("Protected IP components are physically excluded from this implementation")
    print("Clinical validation requires NDA access to full PTL-X system")
    print("="*70)